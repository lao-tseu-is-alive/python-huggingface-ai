# python-huggingface-ai
![Hugging Face](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)

Using [huggingface](https://huggingface.co/) [transformers](https://huggingface.co/docs/transformers/index)

## DESCRIPTION
This is a repo of python programs that uses huggingface transformers to
perform various AI task on text.

## NOTES

#### list the local models,sizes, and last accessed time:
```bash
  huggingface-cli scan-cache
```
#### Offline mode
Run 🤗 Transformers in a firewalled or [offline environment](https://huggingface.co/docs/transformers/installation#offline-mode)
with locally cached files by setting the environment variable HF_HUB_OFFLINE to 1.

    export HF_DATASETS_OFFLINE=1 
    export HF_HUB_OFFLINE=1






## INSTALLATION

### 1. Cuda Installation v12.8.0 and cudnn v9.7.1 (needed for tensorflow)
on Ubuntu 24.04
+ [cuda installation](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_local)
+ [cudnn installation](https://developer.nvidia.com/cudnn-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_local)

```bash
mkdir -p ~/Downloads/cuda/
cd ~/Downloads/cuda/
sudo dpkg -i cuda-repo-ubuntu2404-12-8-local_12.8.0-570.86.10-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2404-12-8-local/cuda-47045A0D-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-8
wget https://developer.download.nvidia.com/compute/cudnn/9.7.1/local_installers/cudnn-local-repo-ubuntu2404-9.7.1_1.0-1_amd64.deb
sudo dpkg -i cudnn-local-repo-ubuntu2404-9.7.1_1.0-1_amd64.deb
sudo cp /var/cudnn-local-repo-ubuntu2404-9.7.1/cudnn-local-40C05781-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cudnn

```
### 2. Install tensorflow
+ [tensorflow installation](https://www.tensorflow.org/install)
```bash
pip install tensorflow
```

### 3. Install huggingface transformers
+ [huggingface transformers](https://huggingface.co/transformers/installation)
```bash
pip install transformers
```

