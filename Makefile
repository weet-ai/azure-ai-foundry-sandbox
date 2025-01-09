az-mac:
	brew install azure-cli && \
	echo "az cli ml - workaround for marshmallow issue" && \
	opt/homebrew/Cellar/azure-cli/2.67.0_1/libexec/bin/python -m pip install marshmallow==3.23.2 && \
	az extension add -n ml

az-linux:
	curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash && \
	echo "az cli ml - workaround for marshmallow issue" && \
	/opt/az/bin/python3 -m pip install marshmallow==3.23.2 && \
	az extension add -n ml