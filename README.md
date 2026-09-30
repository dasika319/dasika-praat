# 手机操作指南：用 GitHub 云端 Mac 生成 .dmg

## ⚠️ 强烈建议
上传这一步最好在任意一台电脑上花 10 分钟完成（网吧、同学电脑都行，
因为打包在云端，电脑好坏无所谓）。手机也能做，就是步骤繁琐一些。

## 手机版步骤（安卓/iPhone 通用）

### 第 1 步：解压并准备好 6 个文件
把 VoiceAnalysisApp.zip 解压，里面应有：
- main.py
- run_app.py
- requirements.txt
- VoiceAnalysisApp.spec
- assets.py
- .github 文件夹（里面的内容最后单独处理，见第 4 步）

### 第 2 步：注册并建仓库
1. 浏览器打开 github.com（推荐 Chrome），Sign up 注册
2. 登录后点右上角头像或 ≡ 菜单 → Your repositories → New
3. 名字填 voice-app，选 Public，Create repository
4. 如果页面很难点：浏览器菜单里勾选"桌面版网站/Desktop site"

### 第 3 步：上传 5 个文件
1. 仓库页面点 Add file → Upload files
2. 点 choose your files，文件选择器里**长按可多选**，
   一次选中那 5 个 .py / .txt / .spec 文件
3. 点 Commit changes 确认上传

### 第 4 步：添加工作流（唯一需要打字的一步）
1. 回到仓库首页，Add file → Create new file
2. 文件名处输入（斜杠会帮我们自动建文件夹）：
   .github/workflows/build-dmg.yml
3. 把 build-dmg.yml 文件里的全部内容复制粘贴到正文
   （用手机上的文本编辑器打开 .yml 文件 → 全选 → 复制）
4. 点 Commit changes

### 第 5 步：点按钮，云端 Mac 开始打包
1. 仓库上方点 Actions
2. 第一次会要求启用：点绿色 I understand my workflows... enable
3. 左侧点 Build macOS DMG → 右侧 Run workflow → 再点一次绿色按钮

### 第 6 步：下载成品
1. 等 5~10 分钟，黄点变绿 = 成功；变红 = 失败（把报错截图发给帮你的人）
2. 点进那次运行记录，拉到页面最底部 Artifacts
3. 点 VoiceAnalysisTool-dmg 下载（是个 zip）
4. 用手机文件管理器解压，里面就是要交的 VoiceAnalysisTool.dmg

## 常见问题
- iPhone 解压 zip：文件 App 里长按 zip → 解压缩
- 安卓解压：文件管理器一般自带，或用 ZArchiver
- dmg 交给老师：从手机用邮件/QQ/微信发出去即可
