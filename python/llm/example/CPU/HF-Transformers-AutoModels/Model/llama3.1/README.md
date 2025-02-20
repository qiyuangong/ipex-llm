# Llama3.1
In this directory, you will find examples on how you could apply IPEX-LLM INT4 optimizations on Llama3.1 models. For illustration purposes, we utilize the [meta-llama/Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) as a reference Llama3.1 model.

## 0. Requirements
To run these examples with IPEX-LLM, we have some recommended requirements for your machine, please refer to [here](../README.md#recommended-requirements) for more information.

## Example: Predict Tokens using `generate()` API
In the example [generate.py](./generate.py), we show a basic use case for a Llama3.1 model to predict the next N tokens using `generate()` API, with IPEX-LLM INT4 optimizations.
### 1. Install
We suggest using conda to manage environment:

On Linux:

```bash
conda create -n llm python=3.11
conda activate llm

# install ipex-llm with 'all' option
pip install --pre --upgrade ipex-llm[all] --extra-index-url https://download.pytorch.org/whl/cpu

# transformers>=4.43.1 is required for Llama3.1 with IPEX-LLM optimizations
pip install transformers==4.43.1
pip install "trl<0.12.0" 
```
On Windows:

```cmd
conda create -n llm python=3.11
conda activate llm

pip install --pre --upgrade ipex-llm[all]

pip install transformers==4.43.1
pip install "trl<0.12.0" 
```

### 2. Run
```
python ./generate.py --repo-id-or-model-path REPO_ID_OR_MODEL_PATH --prompt PROMPT --n-predict N_PREDICT
```

Arguments info:
- `--repo-id-or-model-path REPO_ID_OR_MODEL_PATH`: argument defining the huggingface repo id for the Llama3.1 model (e.g. `meta-llama/Meta-Llama-3.1-8B-Instruct`) to be downloaded, or the path to the huggingface checkpoint folder. It is default to be `'meta-llama/Meta-Llama-3.1-8B-Instruct'`.
- `--prompt PROMPT`: argument defining the prompt to be infered (with integrated prompt format for chat). It is default to be `'What is AI?'`.
- `--n-predict N_PREDICT`: argument defining the max number of tokens to predict. It is default to be `32`.

> **Note**: When loading the model in 4-bit, IPEX-LLM converts linear layers in the model into INT4 format. In theory, a *X*B model saved in 16-bit will requires approximately 2*X* GB of memory for loading, and ~0.5*X* GB memory for further inference.
>
> Please select the appropriate size of the Llama3.1 model based on the capabilities of your machine.

#### 2.1 Client
On client Windows machine, it is recommended to run directly with full utilization of all cores:
```cmd
python ./generate.py 
```

#### 2.2 Server
For optimal performance on server, it is recommended to set several environment variables (refer to [here](../README.md#best-known-configuration-on-linux) for more information), and run the example with all the physical cores of a single socket.

E.g. on Linux,
```bash
# set IPEX-LLM env variables
source ipex-llm-init

# e.g. for a server with 48 cores per socket
export OMP_NUM_THREADS=48
numactl -C 0-47 -m 0 python ./generate.py
```

#### 2.3 Sample Output
#### [meta-llama/Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)
```log
Inference time: xxxx s
-------------------- Prompt --------------------
<|begin_of_text|><|start_header_id|>user<|end_header_id|>

What is AI?<|eot_id|><|start_header_id|>assistant<|end_header_id|>


-------------------- Output (skip_special_tokens=False) --------------------
<|begin_of_text|><|begin_of_text|><|start_header_id|>user<|end_header_id|>

What is AI?<|eot_id|><|start_header_id|>assistant<|end_header_id|>

Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans. The term may also be applied to
```
