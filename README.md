# x64_WinQSB
The 64-bit WinQSB installer is designed for Windows 10 and 11, allowing direct installation and运行 without a virtual machine, simplifying the setup on 64-bit systems.
# 64位 WinQSB 安装向导 开发文档

## 项目概述

### 项目名称
64位 WinQSB 安装向导

### 项目目标
本项目旨在提供一个简单易用的安装向导，用于在64位Windows操作系统上安装并运行WinQSB软件。通过集成OTVDM（Open Tapioca Virtual DOS Machine），确保WinQSB能够在现代64位系统中正常运行。

## 项目文件结构


### 文件说明

#### 根目录
- **build**: 编译输出目录。
- **dist**: 打包后的可执行文件输出目录。
- **License**: 许可证文件。
- **resource**: 资源文件目录。
- **venv**: Python虚拟环境目录。

#### 源代码文件
- **App.py**: 主应用程序入口文件。
- **App.spec**: PyInstaller 生成的配置文件。
- **CheckVCRuntimesThread.py**: 检查VC运行时线程的脚本。
- **common.py**: 公共函数和工具类。
- **init.py**: 初始化文件。
- **MainGui.py**: 主界面逻辑文件。
- **OT_MainGui.ui**: 主界面的UI文件（使用Qt Designer设计）。
- **MyMainWindow.py**: 自定义主窗口类。
- **WinQSB version info.txt**: WinQSB 版本信息文件。

#### 文档文件
- **开发文档.md**: 项目开发文档。
- **开发环境.md**: 项目开发环境配置文档。

## 实现原理

### 安装流程
1. **启动安装向导**：用户启动安装向导后，首先会看到欢迎界面。
2. **秘钥验证**：
   - 生成一个随机数。
   - 将该随机数加1。
   - 将结果转换为16进制字符串作为秘钥。
   - 用户输入秘钥进行验证。
   - 验证通过后，继续下一步。
3. **运行OTVDM**：启动OTVDM虚拟机。
4. **运行WinQSB**：在OTVDM中启动WinQSB软件。

### 秘钥验证方法
1. **生成随机数**：使用系统随机数生成器生成一个随机整数。
2. **计算秘钥**：将随机数加1，然后将结果转换为16进制字符串。
3. **用户输入**：用户输入秘钥进行验证。
4. **验证逻辑**：将用户输入的秘钥与计算出的秘钥进行比较，如果匹配则验证通过，否则提示错误。

### 技术栈
- **Python**：主要编程语言
- **PyQt6**：图形用户界面库
- **OTVDM**：虚拟DOS环境
- **WinQSB**：目标应用程序

## 更新日志

### 2024年11月7日
- **优化安装包存放路径**：将安装包存放在更整齐规范的目录结构中，方便管理和维护。
- **支付窗口和联系作者窗口**：将支付窗口和联系作者窗口设计为圆角矩形，提升用户体验。
- **优化系统通知显示格式**：改进系统通知的显示格式，使其更加清晰和美观。

## 详细设计

### 目录结构
- **build**: 编译输出目录，用于存放中间文件。
- **dist**: 打包后的可执行文件输出目录，最终发布版本将存放于此。
- **License**: 许可证文件，包含项目的许可信息。
- **resource**: 资源文件目录，存放图标、样式表等资源文件。
- **venv**: Python虚拟环境目录，用于隔离项目依赖。

### 主要模块

#### `App.py`
- **功能**：主入口文件，负责初始化应用和显示主窗口。

#### `MainGui.py`
- **功能**：主界面逻辑文件，处理用户交互和业务逻辑。

#### `common.py`
- **功能**：公共函数和工具类，提供秘钥生成和验证等功能。

#### `OT_MainGui.ui`
- **功能**：主界面的UI文件，使用Qt Designer设计。

#### `MyMainWindow.py`
- **功能**：自定义主窗口类，扩展主界面的功能。

#### `WinQSB version info.txt`
- **功能**：记录WinQSB的版本信息。

D:\code\Pythonly winQs
├── build
├── dist
├── License
├── resource
├── venv
├── App.py
├── App.spec
├── CheckVCRuntimesThread.py
├── common.py
├── init.py
├── MainGui.py
├── OT_MainGui.ui
├── MyMainWindow.py
├── WinQSB version info.txt
├── 开发文档.md
└── 开发环境.md

# 64-bit WinQSB Installer Guide Development Documentation

## Project Overview

### Project Name
64-bit WinQSB Installer Guide

### Project Objective
This project aims to provide an easy-to-use installer for installing and running WinQSB software on 64-bit Windows operating systems. By integrating OTVDM (Open Tapioca Virtual DOS Machine), it ensures WinQSB runs smoothly on modern 64-bit systems.

## Project File Structure

### File Descriptions

#### Root Directory
- **build**: Compilation output directory.
- **dist**: Packaged executable output directory.
- **License**: License file.
- **resource**: Resource files directory.
- **venv**: Python virtual environment directory.

#### Source Code Files
- **App.py**: Main application entry file.
- **App.spec**: PyInstaller configuration file.
- **CheckVCRuntimesThread.py**: Script to check VC runtimes.
- **common.py**: Common functions and utility classes.
- **init.py**: Initialization file.
- **MainGui.py**: Main GUI logic file.
- **OT_MainGui.ui**: Main UI file designed with Qt Designer.
- **MyMainWindow.py**: Custom main window class.
- **WinQSB version info.txt**: WinQSB version information file.

#### Documentation Files
- **Development Documentation.md**: Project development documentation.
- **Development Environment.md**: Project development environment setup documentation.

## Implementation Principles

### Installation Process
1. **Launch Installer**: User starts the installer and sees a welcome screen.
2. **Key Verification**:
   - Generate a random number.
   - Increment it by one.
   - Convert the result to a hexadecimal string as the key.
   - User inputs the key for verification.
   - Proceed to the next step if verified.
3. **Run OTVDM**: Launch the OTVDM virtual machine.
4. **Run WinQSB**: Start WinQSB within OTVDM.

### Key Verification Method
1. **Generate Random Number**: Use a system random number generator.
2. **Calculate Key**: Increment the random number and convert to a hexadecimal string.
3. **User Input**: User inputs the key for verification.
4. **Verification Logic**: Compare user input with the calculated key; match passes, otherwise error.

### Technology Stack
- **Python**: Primary programming language.
- **PyQt6**: GUI library.
- **OTVDM**: Virtual DOS environment.
- **WinQSB**: Target application.

## Changelog

### November 7, 2024
- **Optimized Package Path**: Neatened the directory structure for easier management.
- **Payment and Contact Window Design**: Rounded corners for a better user experience.
- **System Notification Format**: Improved display format for clarity and aesthetics.

## Detailed Design

### Directory Structure
- **build**: For intermediate compilation files.
- **dist**: Final packaged executables.
- **License**: Contains licensing information.
- **resource**: Icons, stylesheets, etc.
- **venv**: Isolated Python environment for dependencies.

### Main Modules

#### `App.py`
- **Functionality**: Initializes the app and displays the main window.

#### `MainGui.py`
- **Functionality**: Handles user interaction and business logic.

#### `common.py`
- **Functionality**: Provides key generation and verification utilities.

#### `OT_MainGui.ui`
- **Functionality**: Main UI file designed with Qt Designer.

#### `MyMainWindow.py`
- **Functionality**: Extends main interface functionality.

#### `WinQSB version info.txt`
- **Functionality**: Records WinQSB version information.
