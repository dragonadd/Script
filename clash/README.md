## 自用 ACL4SSR_Online_Mannix.ini



;去广告：支持

;自动测速：支持

;微软分流：支持

;游戏分流：支持

;增强中国IP段：支持

;增强国外GFW：支持

https://raw.githubusercontent.com/dragonadd/Script/main/clash/ACL4SSR_Online_Mannix.ini

### 修改说明

以**精简版 带故障转移**分组为模板，

添加了Ⓜ️ 微软服务、🎮 游戏平台、🛑 广告拦截、🍃 应用净化

附带张浩名字

### 模式介绍：

> - 延迟最低，顾名思义，每隔一段时间进行延迟测试，选择延迟最低的节点
> - 故障转移，每次都选组内第一个节点，无法使用再换到第二个，依次类推
> - 手动选择，顾名思义，没有特殊功能
> - 负载均衡，每个节点都用用，由于很多机场都有连接数的限制，因此实际使用较少

### 关于url-test

- 延迟测试链接 http://www.gstatic.com/generate_204`300,,50

- `300,,50` 是 Subconverter 配置中一个紧凑的参数写法，分别代表了 **测速间隔**、**测速超时** 和 **延迟容差** 这三个核心参数。

  具体含义如下：

  | 参数           | 值     | 含义                                                         |
  | -------------- | ------ | ------------------------------------------------------------ |
  | **第一个参数** | `300`  | **测速间隔**：每 **300秒**（即5分钟）自动对所有节点进行一次测速。 |
  | **第二个参数** | *(空)* | **测速超时**：这里是空的，因此使用默认值 **5秒**。即如果一个节点在5秒内无响应，就被认为测速失败。 |
  | **第三个参数** | `50`   | **延迟容差**：**50毫秒**。当新节点比当前节点的延迟低，但差距小于50ms时，**不会**切换，避免策略频繁变动。 |

  这里的两个逗号 (`,,`) 是作为**占位符**，用来分隔这三个参数。如果你需要调整超时时间，可以在中间填入数字，例如 `300,10,50` 就表示超时时间为10秒。

**其他的测速延迟测试api接口介绍：**

[google谷歌测速延迟测试api通讯接口generate_204 国内阿里云淘宝test 小米华为steam阿卡迈cf](https://bbs.itzmx.com/thread-96457-1-1.html)

[Am I online? 连通性检测成熟方案](https://zhuanlan.zhihu.com/p/1941795511632888522)



### 关于ACL4SSR各ini说明

[acl4ssr仓库指路](https://github.com/acl4ssr/acl4ssr)

[ACL4SSR_Online 默认版 分组比较全 ](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online.ini)

[ACL4SSR_Online_AdblockPlus 更多去广告 ](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_AdblockPlus.ini)

[ACL4SSR_Online_NoAuto 无自动测速 ](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_NoAuto.ini)

[ACL4SSR_Online_NoReject 无广告拦截规则 ](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_NoReject.ini)

[ACL4SSR_Online_Mini 精简版 ](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Mini.ini)

[ACL4SSR_Online_Mini_AdblockPlus.ini 精简版 更多去广告 ](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Mini_AdblockPlus.ini)

[ACL4SSR_Online_Mini_NoAuto.ini 精简版 不带自动测速 ](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Mini_NoAuto.ini)

[ACL4SSR_Online_Mini_Fallback.ini 精简版 带故障转移 

[](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Mini_Fallback.ini)
[ACL4SSR_Online_Mini_MultiMode.ini 精简版 自动测速、故障转移、负载均衡 ](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Mini_MultiMode.ini)

[ACL4SSR_Online_Full 全分组 重度用户使用 ](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Full.ini)[ACL4SSR_Online_Full_MultiMode.ini全分组多模式重度用户使用](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Full_MultiMode.ini)

[ACL4SSR_Online_Full_NoAuto.ini 全分组 无自动测速 重度用户使用 ](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Full_NoAuto.ini)

[ACL4SSR_Online_Full_AdblockPlus 全分组 重度用户使用 更多去广告 ](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Full_AdblockPlus.ini)

[ACL4SSR_Online_Full_Netflix 全分组 重度用户使用 奈飞全量 ](https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Full_Netflix.ini)

# 趣味ini

https://raw.githubusercontent.com/dragonadd/Script/main/clash/update.ini

### 修改说明

以**精简版**分组为模板，

更改了节点选择名字
