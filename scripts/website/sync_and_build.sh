#!/bin/bash

# Configuration
REPO_PATH="/Users/cs/work/AgentNetworkProtocol"
WEBSITE_PATH="$REPO_PATH/scripts/website"
LOG_FILE="$WEBSITE_PATH/sync.log"
LOCK_FILE="/tmp/mcp_website_sync.lock"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Check if another instance is running
if [ -f "$LOCK_FILE" ]; then
    pid=$(cat "$LOCK_FILE")
    if ps -p "$pid" > /dev/null; then
        log "Another sync process is already running. Exiting."
        exit 1
    fi
fi

# Create lock file
echo $$ > "$LOCK_FILE"

# Cleanup function
cleanup() {
    rm -f "$LOCK_FILE"
    log "Sync process completed"
}
trap cleanup EXIT

# Start sync process
log "Starting sync process..."

# Navigate to repo directory
cd "$REPO_PATH" || {
    log "Error: Could not change to repository directory"
    exit 1
}

# Fetch latest changes
log "Fetching latest changes..."
git fetch origin || {
    log "Error: Git fetch failed"
    exit 1
}

# Check if there are any changes
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse @{u})

if [ "$LOCAL" = "$REMOTE" ]; then
    log "No changes detected. Skipping build."
    exit 0
fi

# Pull changes
log "Changes detected. Pulling updates..."
git pull origin main || {
    log "Error: Git pull failed"
    exit 1
}

# Navigate to website directory and build
cd "$WEBSITE_PATH" || {
    log "Error: Could not change to website directory"
    exit 1
}

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    log "Installing dependencies..."
    npm install || {
        log "Error: npm install failed"
        exit 1
    }
fi

# Build website
log "Building website..."
npm run docs:build || {
    log "Error: Website build failed"
    exit 1
}

log "Website sync and build completed successfully"
