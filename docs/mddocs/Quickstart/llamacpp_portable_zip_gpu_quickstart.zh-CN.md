#  使用 IPEX-LLM 在 Intel GPU 运行 llama.cpp Portable Zip 
<p>
   < <a href='./llamacpp_portable_zip_gpu_quickstart.md'>English</a> | <b>中文</b> >
</p>
     
本指南演示如何使用 [llama.cpp portable zip](https://github.com/ipex-llm/ipex-llm/releases/tag/v2.2.0) 通过 `ipex-llm` 在 Intel GPU 上直接免安装运行。

> [!Important]
> 使用最新版 *llama.cpp Portable Zip* 可以在 Xeon 上通过1到2张 Arc A770 GPU 运行 **DeepSeek-R1-671B-Q4_K_M**；详见如下[指南](#flashmoe-运行-deepseek-v3r1)。

> [!NOTE]
> llama.cpp portable zip 在如下设备上进行了验证：
> - Intel Core Ultra processors
> - Intel Core 11th - 14th gen processors
> - Intel Arc A-Series GPU
> - Intel Arc B-Series GPU

## 目录
- [Windows 用户指南](#windows-用户指南)
  - [系统环境安装](#系统环境安装)
  - [步骤 1：下载与解压](#步骤-1下载与解压)
  - [步骤 2：运行时配置](#步骤-2运行时配置)
  - [步骤 3：运行 GGUF 模型](#步骤-3运行-gguf-模型)
- [Linux 用户指南](#linux-用户指南)
  - [系统环境安装](#系统环境安装-1)
  - [步骤 1：下载与解压](#步骤-1下载与解压-1)
  - [步骤 2：运行时配置](#步骤-2运行时配置-1)
  - [步骤 3：运行 GGUF 模型](#步骤-3运行-gguf-模型-1)
  - [(新功能) FlashMoE 运行 DeepSeek V3/R1 671B](#flashmoe-运行-deepseek-v3r1)
- [提示与故障排除](#提示与故障排除)
  - [错误：检测到不同的 sycl 设备](#错误检测到不同的-sycl-设备)
  - [多 GPU 配置](#多-gpu-配置)
  - [性能环境](#性能环境)
  - [签名验证](#签名验证)
- [更多详情](llama_cpp_quickstart.md)

## Windows 用户指南

### 系统环境安装

我们推荐将你的 GPU 驱动版本升级到[最新版本](https://www.intel.com/content/www/us/en/download/785597/intel-arc-iris-xe-graphics-windows.html)。

### 步骤 1：下载与解压

对于 Windows 用户，请从此[链接](https://github.com/ipex-llm/ipex-llm/releases/tag/v2.2.0)下载 IPEX-LLM llama.cpp portable zip。

然后，将 zip 文件解压到一个文件夹中。

### 步骤 2：运行时配置

- 打开命令提示符（cmd），并通过在命令行输入指令 `cd /d PATH\TO\EXTRACTED\FOLDER` 进入解压缩后的文件夹。
- 对于多 GPU 用户，请转至[提示](#多-gpu-配置)了解如何选择特定的 GPU。

### 步骤 3：运行 GGUF 模型

这里我们提供了一个简单的示例来展示如何使用 IPEX-LLM 运行社区 GGUF 模型。

#### 模型下载
运行之前，你需要下载或复制社区的 GGUF 模型到你的当前目录。例如，[bartowski/DeepSeek-R1-Distill-Qwen-7B-GGUF](https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-7B-GGUF/blob/main/DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf) 的 `DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf`。

#### 运行 GGUF 模型

在运行以下命令之前，请将 `PATH\TO\DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf` 更改为你的模型路径。

```cmd
llama-cli.exe -m PATH\TO\DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf -p "A conversation between User and Assistant. The user asks a question, and the Assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides the user with the answer. The reasoning process and answer are enclosed within <think> </think> and <answer> </answer> tags, respectively, i.e., <think> reasoning process here </think> <answer> answer here </answer>. User: Question:The product of the ages of three teenagers is 4590. How old is the oldest? a. 18 b. 19 c. 15 d. 17 Assistant: <think>" -n 2048  -t 8 -e -ngl 99 --color -c 2500 --temp 0 -no-cnv
```

部分输出：

```
Found 1 SYCL devices:
|  |                   |                                       |       |Max    |        |Max  |Global |                     |
|  |                   |                                       |       |compute|Max work|sub  |mem    |                     |
|ID|        Device Type|                                   Name|Version|units  |group   |group|size   |       Driver version|
|--|-------------------|---------------------------------------|-------|-------|--------|-----|-------|---------------------|
| 0| [level_zero:gpu:0]|                Intel Arc A770 Graphics|  12.55|    512|    1024|   32| 16225M|     1.6.31294.120000|
SYCL Optimization Feature:
|ID|        Device Type|Reorder|
|--|-------------------|-------|
| 0| [level_zero:gpu:0]|      Y|
llama_kv_cache_init: kv_size = 2528, offload = 1, type_k = 'f16', type_v = 'f16', n_layer = 28, can_shift = 1
llama_kv_cache_init:      SYCL0 KV buffer size =   138.25 MiB
llama_init_from_model: KV self size  =  138.25 MiB, K (f16):   69.12 MiB, V (f16):   69.12 MiB
llama_init_from_model:  SYCL_Host  output buffer size =     0.58 MiB
llama_init_from_model:      SYCL0 compute buffer size =  1501.00 MiB
llama_init_from_model:  SYCL_Host compute buffer size =    59.28 MiB
llama_init_from_model: graph nodes  = 874
llama_init_from_model: graph splits = 2
common_init_from_params: setting dry_penalty_last_n to ctx_size = 2528
common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
main: llama threadpool init, n_threads = 8

system_info: n_threads = 8 (n_threads_batch = 8) / 32 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 1 | F16C = 1 | FMA = 1 | LLAMAFILE = 1 | OPENMP = 1 | AARCH64_REPACK = 1 | 

sampler seed: 1856767110
sampler params: 
        repeat_last_n = 64, repeat_penalty = 1.000, frequency_penalty = 0.000, presence_penalty = 0.000
        dry_multiplier = 0.000, dry_base = 1.750, dry_allowed_length = 2, dry_penalty_last_n = 2528
        top_k = 40, top_p = 0.950, min_p = 0.050, xtc_probability = 0.000, xtc_threshold = 0.100, typical_p = 1.000, top_n_sigma = -1.000, temp = 0.000
        mirostat = 0, mirostat_lr = 0.100, mirostat_ent = 5.000
sampler chain: logits -> logit-bias -> penalties -> dry -> top-k -> typical -> top-p -> min-p -> xtc -> temp-ext -> dist 
generate: n_ctx = 2528, n_batch = 4096, n_predict = 2048, n_keep = 1

<think>
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
</think>

<answer>XXXX</answer> [end of text]


llama_perf_sampler_print:    sampling time =     xxx.xx ms /  1386 runs   (    x.xx ms per token, xxxxx.xx tokens per second)
llama_perf_context_print:        load time =   xxxxx.xx ms
llama_perf_context_print: prompt eval time =     xxx.xx ms /   129 tokens (    x.xx ms per token,   xxx.xx tokens per second)
llama_perf_context_print:        eval time =   xxxxx.xx ms /  1256 runs   (   xx.xx ms per token,    xx.xx tokens per second)
llama_perf_context_print:       total time =   xxxxx.xx ms /  1385 tokens
```

## Linux 用户指南

### 系统环境安装

检查你的 GPU 驱动程序版本，并根据需要进行更新；我们推荐用户按照 [消费级显卡驱动安装指南](https://dgpu-docs.intel.com/driver/client/overview.html)来安装 GPU 驱动。

### 步骤 1：下载与解压

对于 Linux 用户，从此[链接](https://github.com/ipex-llm/ipex-llm/releases/tag/v2.2.0)下载 IPEX-LLM llama.cpp portable tgz。

然后，将 tgz 文件解压到一个文件夹中。

### 步骤 2：运行时配置

- 开启一个终端，输入命令 `cd /PATH/TO/EXTRACTED/FOLDER` 进入解压缩后的文件夹。
- 对于多 GPU 用户，请转至[提示](#多-gpu-配置)了解如何选择特定的 GPU。

### 步骤 3：运行 GGUF 模型

这里我们提供了一个简单的示例来展示如何使用 IPEX-LLM 运行社区 GGUF 模型。  

#### 模型下载
运行之前，你需要下载或复制社区的 GGUF 模型到你的当前目录。例如，[bartowski/DeepSeek-R1-Distill-Qwen-7B-GGUF](https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-7B-GGUF/blob/main/DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf) 的 `DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf`。

#### 运行 GGUF 模型

在运行以下命令之前，请将 `PATH\TO\DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf` 更改为你的模型路径。

```bash
./llama-cli -m /PATH/TO/DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf -p "A conversation between User and Assistant. The user asks a question, and the Assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides the user with the answer. The reasoning process and answer are enclosed within <think> </think> and <answer> </answer> tags, respectively, i.e., <think> reasoning process here </think> <answer> answer here </answer>. User: Question:The product of the ages of three teenagers is 4590. How old is the oldest? a. 18 b. 19 c. 15 d. 17 Assistant: <think>" -n 2048  -t 8 -e -ngl 99 --color -c 2500 --temp 0 -no-cnv
```

部分输出：

```bash
Found 1 SYCL devices:
|  |                   |                                       |       |Max    |        |Max  |Global |                     |
|  |                   |                                       |       |compute|Max work|sub  |mem    |                     |
|ID|        Device Type|                                   Name|Version|units  |group   |group|size   |       Driver version|
|--|-------------------|---------------------------------------|-------|-------|--------|-----|-------|---------------------|
| 0| [level_zero:gpu:0]|                Intel Arc A770 Graphics|  12.55|    512|    1024|   32| 16225M|     1.6.31294.120000|
SYCL Optimization Feature:
|ID|        Device Type|Reorder|
|--|-------------------|-------|
| 0| [level_zero:gpu:0]|      Y|
llama_kv_cache_init: kv_size = 2528, offload = 1, type_k = 'f16', type_v = 'f16', n_layer = 28, can_shift = 1
llama_kv_cache_init:      SYCL0 KV buffer size =   138.25 MiB
llama_init_from_model: KV self size  =  138.25 MiB, K (f16):   69.12 MiB, V (f16):   69.12 MiB
llama_init_from_model:  SYCL_Host  output buffer size =     0.58 MiB
llama_init_from_model:      SYCL0 compute buffer size =  1501.00 MiB
llama_init_from_model:  SYCL_Host compute buffer size =    59.28 MiB
llama_init_from_model: graph nodes  = 874
llama_init_from_model: graph splits = 2
common_init_from_params: setting dry_penalty_last_n to ctx_size = 2528
common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
main: llama threadpool init, n_threads = 8

system_info: n_threads = 8 (n_threads_batch = 8) / 32 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 1 | F16C = 1 | FMA = 1 | LLAMAFILE = 1 | OPENMP = 1 | AARCH64_REPACK = 1 | 

sampler seed: 1856767110
sampler params: 
        repeat_last_n = 64, repeat_penalty = 1.000, frequency_penalty = 0.000, presence_penalty = 0.000
        dry_multiplier = 0.000, dry_base = 1.750, dry_allowed_length = 2, dry_penalty_last_n = 2528
        top_k = 40, top_p = 0.950, min_p = 0.050, xtc_probability = 0.000, xtc_threshold = 0.100, typical_p = 1.000, top_n_sigma = -1.000, temp = 0.000
        mirostat = 0, mirostat_lr = 0.100, mirostat_ent = 5.000
sampler chain: logits -> logit-bias -> penalties -> dry -> top-k -> typical -> top-p -> min-p -> xtc -> temp-ext -> dist 
generate: n_ctx = 2528, n_batch = 4096, n_predict = 2048, n_keep = 1

<think>
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
</think>

<answer>XXXX</answer> [end of text]
```

### FlashMoE 运行 DeepSeek V3/R1

FlashMoE 是一款基于 `llama.cpp` 构建的命令行工具，针对 DeepSeek V3/R1 等混合专家模型（MoE）模型进行了优化。它现可用于 Linux 平台。

经过测试的 MoE GGUF 模型（也支持其他 MoE GGUF 模型）：
- [DeepSeek-V3-Q4_K_M](https://huggingface.co/unsloth/DeepSeek-V3-GGUF/tree/main/DeepSeek-V3-Q4_K_M)
- [DeepSeek-V3-Q6_K](https://huggingface.co/unsloth/DeepSeek-V3-GGUF/tree/main/DeepSeek-V3-Q6_K)
- [DeepSeek-R1-Q4_K_M.gguf](https://huggingface.co/unsloth/DeepSeek-R1-GGUF/tree/main/DeepSeek-R1-Q4_K_M)
- [DeepSeek-R1-Q6_K](https://huggingface.co/unsloth/DeepSeek-R1-GGUF/tree/main/DeepSeek-R1-Q6_K)
- [DeepSeek-V3-0324-GGUF/Q4_K_M](https://huggingface.co/unsloth/DeepSeek-V3-0324-GGUF/tree/main/Q4_K_M)
- [DeepSeek-V3-0324-GGUF/Q6_K](https://huggingface.co/unsloth/DeepSeek-V3-0324-GGUF/tree/main/Q6_K)

硬件要求： 
- 380 GB 内存
- 1-8块 ARC A770
- 500GB 硬盘空间

提示： 
- 更大的模型和其他精度可能需要更多的资源。
- 对于 1 块 ARC A770 的平台，请减少上下文长度（例如 1024），以避免 OOM（内存溢出）。请在以下命令的末尾添加选项 `-c 1024`。
- 对于拥有 2 块 CPU 的平台，请在 BIOS 上开启`子NUMA 集群`, 并在启动命令前增加 `numactl --interleave=all`, 以获得*更高的性能*。

运行之前，你需要下载或复制社区的 GGUF 模型到你的当前目录。例如，[DeepSeek-R1-Q4_K_M.gguf](https://huggingface.co/unsloth/DeepSeek-R1-GGUF/tree/main/DeepSeek-R1-Q4_K_M) 的 `DeepSeek-R1-Q4_K_M.gguf`。

请将 `/PATH/TO/DeepSeek-R1-Q4_K_M-00001-of-00009.gguf` 更改为您的模型路径，然后运行 `DeepSeek-R1-Q4_K_M.gguf`

##### 命令行
```bash
./flash-moe -m /PATH/TO/DeepSeek-R1-Q4_K_M-00001-of-00009.gguf --prompt "What's AI?" -no-cnv
```

部分输出：

```bash
llama_kv_cache_init:      SYCL0 KV buffer size =  1280.00 MiB
llama_kv_cache_init:      SYCL1 KV buffer size =  1280.00 MiB
llama_kv_cache_init:      SYCL2 KV buffer size =  1280.00 MiB
llama_kv_cache_init:      SYCL3 KV buffer size =  1280.00 MiB
llama_kv_cache_init:      SYCL4 KV buffer size =  1120.00 MiB
llama_kv_cache_init:      SYCL5 KV buffer size =  1280.00 MiB
llama_kv_cache_init:      SYCL6 KV buffer size =  1280.00 MiB
llama_kv_cache_init:      SYCL7 KV buffer size =   960.00 MiB
llama_new_context_with_model: KV self size  = 9760.00 MiB, K (i8): 5856.00 MiB, V (i8): 3904.00 MiB
llama_new_context_with_model:  SYCL_Host  output buffer size =     0.49 MiB
llama_new_context_with_model: pipeline parallelism enabled (n_copies=1)
llama_new_context_with_model:      SYCL0 compute buffer size =  2076.02 MiB
llama_new_context_with_model:      SYCL1 compute buffer size =  2076.02 MiB
llama_new_context_with_model:      SYCL2 compute buffer size =  2076.02 MiB
llama_new_context_with_model:      SYCL3 compute buffer size =  2076.02 MiB
llama_new_context_with_model:      SYCL4 compute buffer size =  2076.02 MiB
llama_new_context_with_model:      SYCL5 compute buffer size =  2076.02 MiB
llama_new_context_with_model:      SYCL6 compute buffer size =  2076.02 MiB
llama_new_context_with_model:      SYCL7 compute buffer size =  3264.00 MiB
llama_new_context_with_model:  SYCL_Host compute buffer size =  1332.05 MiB
llama_new_context_with_model: graph nodes  = 5184 (with bs=4096), 4720 (with bs=1)
llama_new_context_with_model: graph splits = 125
common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
main: llama threadpool init, n_threads = 48

system_info: n_threads = 48 (n_threads_batch = 48) / 192 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX_VNNI = 1 | AVX2 = 1 | F16C = 1 | FMA = 1 | LLAMAFILE = 1 | OPENMP = 1 | AARCH64_REPACK = 1 |

sampler seed: 2052631435
sampler params:
        repeat_last_n = 64, repeat_penalty = 1.000, frequency_penalty = 0.000, presence_penalty = 0.000
        dry_multiplier = 0.000, dry_base = 1.750, dry_allowed_length = 2, dry_penalty_last_n = -1
        top_k = 40, top_p = 0.950, min_p = 0.050, xtc_probability = 0.000, xtc_threshold = 0.100, typical_p = 1.000, temp = 0.800
        mirostat = 0, mirostat_lr = 0.100, mirostat_ent = 5.000
sampler chain: logits -> logit-bias -> penalties -> dry -> top-k -> typical -> top-p -> min-p -> xtc -> temp-ext -> dist
generate: n_ctx = 4096, n_batch = 4096, n_predict = -1, n_keep = 1

<think>
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
</think>

<answer>XXXX</answer> [end of text]
```

##### 推理服务
```bash
./flash-moe -m /PATH/TO/DeepSeek-R1-Q4_K_M-00001-of-00009.gguf --serve -n 512 -np 2 -c 4096
```
> `-n`代表预测字符的数目, `-np`代表并行解码序列的数目, `-c`代表整个上下文序列的最大长度，你可以根据你的需要自行调整这些参数数值。
>
> 推理服务需要[v2.3.0 nightly build](https://github.com/ipex-llm/ipex-llm/releases/tag/v2.3.0-nightly)或者更新的版本。

部分输出：

```bash
...
llama_init_from_model: graph nodes  = 3560
llama_init_from_model: graph splits = 121
common_init_from_params: setting dry_penalty_last_n to ctx_size = 4096
common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
srv          init: initializing slots, n_slots = 2
slot         init: id  0 | task -1 | new slot n_ctx_slot = 2048
slot         init: id  1 | task -1 | new slot n_ctx_slot = 2048
main: model loaded
main: chat template, chat_template: {% if not add_generation_prompt is defined %}{% set add_generation_prompt = false %}{% endif %}{% set ns = namespace(is_first=false, is_tool=false, is_output_first=true, system_prompt='', is_first_sp=true) %}{%- for message in messages %}{%- if message['role'] == 'system' %}{%- if ns.is_first_sp %}{% set ns.system_prompt = ns.system_prompt + message['content'] %}{% set ns.is_first_sp = false %}{%- else %}{% set ns.system_prompt = ns.system_prompt + '\n\n' + message['content'] %}{%- endif %}{%- endif %}{%- endfor %}{{ bos_token }}{{ ns.system_prompt }}{%- for message in messages %}{%- if message['role'] == 'user' %}{%- set ns.is_tool = false -%}{{'<｜User｜>' + message['content']}}{%- endif %}{%- if message['role'] == 'assistant' and 'tool_calls' in message %}{%- set ns.is_tool = false -%}{%- for tool in message['tool_calls'] %}{%- if not ns.is_first %}{%- if message['content'] is none %}{{'<｜Assistant｜><｜tool▁calls▁begin｜><｜tool▁call▁begin｜>' + tool['type'] + '<｜tool▁sep｜>' + tool['function']['name'] + '\n' + '```json' + '\n' + tool['function']['arguments'] + '\n' + '```' + '<｜tool▁call▁end｜>'}}{%- else %}{{'<｜Assistant｜>' + message['content'] + '<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>' + tool['type'] + '<｜tool▁sep｜>' + tool['function']['name'] + '\n' + '```json' + '\n' + tool['function']['arguments'] + '\n' + '```' + '<｜tool▁call▁end｜>'}}{%- endif %}{%- set ns.is_first = true -%}{%- else %}{{'\n' + '<｜tool▁call▁begin｜>' + tool['type'] + '<｜tool▁sep｜>' + tool['function']['name'] + '\n' + '```json' + '\n' + tool['function']['arguments'] + '\n' + '```' + '<｜tool▁call▁end｜>'}}{%- endif %}{%- endfor %}{{'<｜tool▁calls▁end｜><｜end▁of▁sentence｜>'}}{%- endif %}{%- if message['role'] == 'assistant' and 'tool_calls' not in message %}{%- if ns.is_tool %}{{'<｜tool▁outputs▁end｜>' + message['content'] + '<｜end▁of▁sentence｜>'}}{%- set ns.is_tool = false -%}{%- else %}{% set content = message['content'] %}{% if '</think>' in content %}{% set content = content.split('</think>')[-1] %}{% endif %}{{'<｜Assistant｜>' + content + '<｜end▁of▁sentence｜>'}}{%- endif %}{%- endif %}{%- if message['role'] == 'tool' %}{%- set ns.is_tool = true -%}{%- if ns.is_output_first %}{{'<｜tool▁outputs▁begin｜><｜tool▁output▁begin｜>' + message['content'] + '<｜tool▁output▁end｜>'}}{%- set ns.is_output_first = false %}{%- else %}{{'<｜tool▁output▁begin｜>' + message['content'] + '<｜tool▁output▁end｜>'}}{%- endif %}{%- endif %}{%- endfor -%}{% if ns.is_tool %}{{'<｜tool▁outputs▁end｜>'}}{% endif %}{% if add_generation_prompt and not ns.is_tool %}{{'<｜Assistant｜>'}}{% endif %}, example_format: 'You are a helpful assistant

<｜User｜>Hello<｜Assistant｜>Hi there<｜end▁of▁sentence｜><｜User｜>How are you?<｜Assistant｜>'
main: server is listening on http://127.0.0.1:8080 - starting the main loop
srv  update_slots: all slots are idle
```


## 提示与故障排除

### 错误：检测到不同的 sycl 设备

你将会看到如下的错误日志：
```
Found 3 SYCL devices:
|  |                   |                                       |       |Max    |        |Max  |Global |                     |
|  |                   |                                       |       |compute|Max work|sub  |mem    |                     |
|ID|        Device Type|                                   Name|Version|units  |group   |group|size   |       Driver version|
|--|-------------------|---------------------------------------|-------|-------|--------|-----|-------|---------------------|
| 0| [level_zero:gpu:0]|                Intel Arc A770 Graphics|  12.55|    512|    1024|   32| 16225M|     1.6.31907.700000|
| 1| [level_zero:gpu:1]|                Intel Arc A770 Graphics|  12.55|    512|    1024|   32| 16225M|     1.6.31907.700000|
| 2| [level_zero:gpu:2]|                 Intel UHD Graphics 770|   12.2|     32|     512|   32| 63218M|     1.6.31907.700000|
Error: Detected different sycl devices, the performance will limit to the slowest device. 
If you want to disable this checking and use all of them, please set environment SYCL_DEVICE_CHECK=0, and try again.
If you just want to use one of the devices, please set environment like ONEAPI_DEVICE_SELECTOR=level_zero:0 or ONEAPI_DEVICE_SELECTOR=level_zero:1 to choose your devices.
If you want to use two or more deivces, please set environment like ONEAPI_DEVICE_SELECTOR="level_zero:0;level_zero:1"
See https://github.com/intel/ipex-llm/blob/main/docs/mddocs/Overview/KeyFeatures/multi_gpus_selection.md for details. Exiting.
```
由于 GPU 规格不同，任务将根据设备的显存进行分配。例如，iGPU（Intel UHD Graphics 770） 将承担 2/3 的计算任务，导致性能表现较差。
为此，你可以有以下两种选择：
1. 禁用 iGPU 可以获得最佳性能。 更多详情可以访问 [多 GPU 配置](#多-gpu-配置)。
2. 禁用此检查并使用所有 GPU，可以运行以下命令：  
   - `set SYCL_DEVICE_CHECK=0` (Windows 用户)   
   - `export SYCL_DEVICE_CHECK=0` (Linux 用户)

### 多 GPU 配置

如果你的机器配有多个 Intel GPU，llama.cpp 默认会在所有 GPU 上运行。如果你不清楚硬件配置，可以在运行 GGUF 模型时获取相关配置信息。例如： 

```
Found 3 SYCL devices:
|  |                   |                                       |       |Max    |        |Max  |Global |                     |
|  |                   |                                       |       |compute|Max work|sub  |mem    |                     |
|ID|        Device Type|                                   Name|Version|units  |group   |group|size   |       Driver version|
|--|-------------------|---------------------------------------|-------|-------|--------|-----|-------|---------------------|
| 0| [level_zero:gpu:0]|                Intel Arc A770 Graphics|  12.55|    512|    1024|   32| 16225M|     1.6.31907.700000|
| 1| [level_zero:gpu:1]|                Intel Arc A770 Graphics|  12.55|    512|    1024|   32| 16225M|     1.6.31907.700000|
```

要指定 llama.cpp 使用的 Intel GPU，可以**在启动 llama.cpp 命令**之前设置环境变量 `ONEAPI_DEVICE_SELECTOR`，示例如下：  

- 对于 **Windows** 用户：
  ```cmd
  set ONEAPI_DEVICE_SELECTOR=level_zero:0 (If you want to run on one GPU, llama.cpp will use the first GPU.) 
  set ONEAPI_DEVICE_SELECTOR="level_zero:0;level_zero:1" (If you want to run on two GPUs, llama.cpp will use the first and second GPUs.)
  ```
- 对于 **Linux** 用户：
  ```bash
  export ONEAPI_DEVICE_SELECTOR=level_zero:0 (If you want to run on one GPU, llama.cpp will use the first GPU.) 
  export ONEAPI_DEVICE_SELECTOR="level_zero:0;level_zero:1" (If you want to run on two GPUs, llama.cpp will use the first and second GPUs.)
  ```
 
### 性能环境
#### SYCL_PI_LEVEL_ZERO_USE_IMMEDIATE_COMMANDLISTS
要启用 SYCL_PI_LEVEL_ZERO_USE_IMMEDIATE_COMMANDLISTS，你可以运行以下命令：
- `set SYCL_PI_LEVEL_ZERO_USE_IMMEDIATE_COMMANDLISTS=1`(Windows 用户)   
- `export SYCL_PI_LEVEL_ZERO_USE_IMMEDIATE_COMMANDLISTS=1`(Linux 用户)

> [!NOTE]
> 环境变量 `SYCL_PI_LEVEL_ZERO_USE_IMMEDIATE_COMMANDLISTS` 用于控制是否使用即时命令列表将任务提交到 GPU。启动此变量通常可以提高性能，但也有例外情况。因此，建议你在启用和禁用该环境变量的情况下进行测试，以找到最佳的性能设置。更多相关细节请参考[此处文章](https://www.intel.com/content/www/us/en/developer/articles/guide/level-zero-immediate-command-lists.html)。  


### 签名验证

针对 2.2.0 版本的 portable zip/tgz, 可以使用如下命令验证其签名：

```
openssl cms -verify -in <portable-zip-or-tgz-file-name>.pkcs1.sig -inform DER -content <portable-zip-or-tgz-file-name> -out nul -noverify
```

> [!NOTE]
> 在验证签名之前，请确保已在系统上安装 `openssl`。