---
title: Chainlit Docker
emoji: 📉
colorFrom: yellow
colorTo: red
sdk: docker
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


STEPS:

Start by cloning this repo by using:

git clone https://huggingface.co/spaces/StefanoDUrso/Chainlit-docker
Create your Dockerfile file:

# read the doc: https://huggingface.co/docs/hub/spaces-sdks-docker
# you will also find guides on how best to write your Dockerfile

FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
Then commit and push:

git add Dockerfile
git commit -m "Add application file"
git push

****** ATTENTION ******
Since October 2023 it is not possible to push using simply username and password: we need to generate a token at HuggingFace and perform the push accordingly: https://huggingface.co/blog/password-git-deprecation

If you don’t have any SSH keys on your machine, you can use ssh-keygen to generate a new SSH key pair (public + private keys):
ssh-keygen -t ed25519 -C "your.email@example.co"

Be sure that the OpenSSH service is STARTED

This generates the couple of keys in the current folder; better to move them into the standard ssh folder (in windows usually c:\users\MYUSERNAME\.ssh; in such scenario we will have something like c:\users\MYUSERNAME\.ssh\ed25519 and inside the pub and private key with the name chosen)

Once your new key is generated, add it to your SSH agent with ssh-add; let's assume we have a key with name id_ed25519 in the folder C:\users\paisl\.ssh\id_ed25519:
ssh-add "C:\users\paisl\.ssh\id_ed25519\id_ed25519"

To add a SSH key to your account, click on the “Add SSH key” button.

Then, enter a name for this key (for example, “Personal computer”), and copy and paste the content of your public SSH key in the area below. The public key is located in the ~/.ssh/id_XXXX.pub file you found or generated in the previous steps.

Click on “Add key”, and voilà! You have added a SSH key to your huggingface.co account.

>ssh -T git@hf.co
The authenticity of host 'hf.co (...)' can't be established.
ED25519 key fingerprint is ...
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'hf.co' (ED25519) to the list of known hosts.
Hi StefanoDUrso, welcome to Hugging Face.

>ssh -T git@hf.co
Hi ..., welcome to Hugging Face.

git remote set-url origin https://MY_GITHUB_NAME:MY_TOKEN@huggingface.co/spaces/MY_HUGGING_FACE_NAME/Chainlit-docker

git pull origin