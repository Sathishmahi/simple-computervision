echo [$(date)] : "Start"
echo "create a conda env"
conda create --prefix pypi_pkg_env python=3.10 -y
echo "activate conda env"
source activate pypi_pkg_env
echo "install requirements"
pip install -r requirements_dev.txt
