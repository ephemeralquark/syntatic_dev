FROM continuumio/miniconda3:22.11.1

EXPOSE 8000

# Install conda dependencies
COPY ../syntactic_web/environment.yml .
RUN conda env update --file environment.yml

# [Optional] Uncomment to install a different version of Python than the default
# RUN conda install -y python=3.6 \
#     && pip install --no-cache-dir pipx \
#     && pipx reinstall-all

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# Set up the shell so it's usable
RUN apt-get update && apt-get -y install --no-install-recommends zsh
RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
