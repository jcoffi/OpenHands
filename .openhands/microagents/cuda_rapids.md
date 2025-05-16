---
name: CUDA and RAPIDS Setup
type: knowledge
version: 1.0.0
agent: CodeActAgent
triggers:
  - CUDA
  - CuPy
  - RAPIDS
---

# CUDA and RAPIDS Setup Microagent

When CUDA, CuPy, or RAPIDS is mentioned in the conversation, I will automatically:

1. Run `nvidia-smi` to check if CUDA is installed and a compatible GPU is available
2. If the command runs successfully and shows that CUDA is installed with a video card:
   - Set or append `/usr/local/cuda/lib64` to the `LD_LIBRARY_PATH` environment variable
   - Run `/openhands/micromamba/bin/micromamba install -y -n base conda-forge::cupy conda-forge::rapids` to install the necessary packages

I will not create any external scripts or files. All actions will be performed directly through bash commands executed within the conversation.

When triggered, I will respond with something like:
"I noticed you mentioned CUDA/CuPy/RAPIDS. Let me check if your system has CUDA installed and set up the necessary libraries for you."

Then I will run the required commands and provide feedback on the results of each step in the process.