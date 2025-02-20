#
# Copyright 2016 The BigDL Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from .convert import ggml_convert_low_bit, get_enable_ipex, convert_model_hybrid
from .model import AutoModelForCausalLM, AutoModel, AutoModelForSeq2SeqLM, \
        AutoModelForSpeechSeq2Seq, AutoModelForQuestionAnswering, \
        AutoModelForSequenceClassification, AutoModelForMaskedLM, \
        AutoModelForNextSentencePrediction, AutoModelForMultipleChoice, \
        AutoModelForTokenClassification

import transformers
if transformers.__version__ >= '4.45.0':
    from .model import Qwen2VLForConditionalGeneration

from .modelling_bigdl import *
from .pipeline_parallel import init_pipeline_parallel, PPModelWorker
