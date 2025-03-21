#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
检测仓库中包含空格的文件名并将空格替换为中划线

用法:
  python3 replace_spaces_with_hyphens.py [选项]

选项:
  -h, --help            显示此帮助信息
  -d, --detect-only     仅检测，不进行重命名
  -y, --yes             自动确认，无需用户交互
  -r, --recursive-dirs  同时处理目录名
  -l, --lowercase       同时将文件名转为小写
  -p PATH, --path PATH  指定要处理的路径（默认为当前仓库根目录）
  --log FILE            指定日志文件（默认为不记录日志）
"""

import os
import sys
import logging
import argparse
from pathlib import Path
from datetime import datetime

def setup_logger(log_file=None):
    """设置日志记录器"""
    logger = logging.getLogger('file_renamer')
    logger.setLevel(logging.INFO)
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # 如果指定了日志文件，创建文件处理器
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    
    return logger

def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='检测仓库中包含空格的文件名并将空格替换为中划线')
    parser.add_argument('-d', '--detect-only', action='store_true', help='仅检测，不进行重命名')
    parser.add_argument('-y', '--yes', action='store_true', help='自动确认，无需用户交互')
    parser.add_argument('-r', '--recursive-dirs', action='store_true', help='同时处理目录名')
    parser.add_argument('-l', '--lowercase', action='store_true', help='同时将文件名转为小写')
    parser.add_argument('-p', '--path', default=None, help='指定要处理的路径（默认为当前仓库根目录）')
    parser.add_argument('--log', default=None, help='指定日志文件（默认为不记录日志）')
    
    return parser.parse_args()

def find_items_with_spaces(base_path, include_dirs=False, exclude_dirs=None):
    """查找包含空格的文件和目录"""
    if exclude_dirs is None:
        exclude_dirs = {'.git', 'node_modules', '__pycache__', 'venv', '.venv'}
    
    items_with_spaces = []
    
    for root, dirs, files in os.walk(base_path):
        # 排除指定目录
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.')]
        
        # 检查文件
        for file in files:
            if ' ' in file:
                file_path = os.path.join(root, file)
                items_with_spaces.append(file_path)
        
        # 如果需要，检查目录
        if include_dirs:
            for dir_name in dirs:
                if ' ' in dir_name:
                    dir_path = os.path.join(root, dir_name)
                    items_with_spaces.append(dir_path)
    
    return items_with_spaces

def rename_items(items, logger, lowercase=False):
    """重命名文件和目录"""
    success_count = 0
    fail_count = 0
    
    # 首先处理文件，然后处理目录（从深到浅）
    # 确保先处理文件，再处理目录
    files = [item for item in items if os.path.isfile(item)]
    dirs = [item for item in items if os.path.isdir(item)]
    # 目录从深到浅排序，确保先处理子目录
    dirs.sort(key=lambda x: x.count(os.sep), reverse=True)
    
    # 处理所有项目
    for item_path in files + dirs:
        dir_path = os.path.dirname(item_path)
        old_name = os.path.basename(item_path)
        
        # 将空格替换为中划线，可选转为小写
        new_name = old_name.replace(' ', '-')
        if lowercase:
            new_name = new_name.lower()
            
        # 如果名称没有变化，跳过
        if new_name == old_name:
            logger.info(f"跳过 (无需更改): {item_path}")
            continue
            
        new_path = os.path.join(dir_path, new_name)
        
        try:
            os.rename(item_path, new_path)
            logger.info(f"已重命名: {item_path} → {new_path}")
            success_count += 1
        except Exception as e:
            logger.error(f"重命名失败: {item_path}")
            logger.error(f"错误信息: {str(e)}")
            fail_count += 1
    
    return success_count, fail_count

def main():
    """主函数"""
    args = parse_arguments()
    
    # 设置日志记录器
    logger = setup_logger(args.log)
    
    # 获取仓库根目录
    if args.path:
        base_path = Path(args.path).resolve()
    else:
        base_path = Path(__file__).parent.parent.resolve()
    
    os.chdir(base_path)
    
    logger.info("=== 文件名空格替换工具 ===")
    logger.info(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"工作目录: {os.getcwd()}")
    
    # 查找包含空格的项目
    items_with_spaces = find_items_with_spaces(
        base_path='.',
        include_dirs=args.recursive_dirs
    )
    
    # 检查结果
    if not items_with_spaces:
        logger.info("未发现包含空格的文件或目录名。")
        return
    
    # 分类统计
    file_count = sum(1 for item in items_with_spaces if os.path.isfile(item))
    dir_count = sum(1 for item in items_with_spaces if os.path.isdir(item))
    
    logger.info(f"发现 {len(items_with_spaces)} 个包含空格的项目:")
    logger.info(f"  文件: {file_count} 个")
    logger.info(f"  目录: {dir_count} 个")
    
    for item in items_with_spaces:
        logger.info(f"  {item}")
    logger.info("")
    
    # 如果只是检测模式，到此结束
    if args.detect_only:
        logger.info("检测完成，因设置了仅检测模式，不进行重命名操作。")
        return
    
    # 询问用户是否继续
    if not args.yes:
        confirm = input("是否将这些项目名中的空格替换为中划线？(y/n): ")
        if confirm.lower() != 'y':
            logger.info("操作已取消。")
            return
    
    # 重命名项目
    logger.info("开始重命名...")
    success_count, fail_count = rename_items(
        items_with_spaces,
        logger,
        lowercase=args.lowercase
    )
    
    logger.info("")
    logger.info("操作完成：")
    logger.info(f"  成功重命名: {success_count} 个项目")
    logger.info(f"  重命名失败: {fail_count} 个项目")
    logger.info(f"结束时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if fail_count > 0:
        logger.warning("注意: 部分项目重命名失败，可能是因为权限问题或文件正在使用中。")

if __name__ == "__main__":
    main()