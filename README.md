# Projet-Marketplace
Marketplace ou place de marché est un site qui rassemble un ou plusieurs acheteurs et vendeurs pour effectuer une transaction commerciale. De manière générale, vous trouverez sur les Marketplaces des produits physiques (DVD, livre…), mais vous pourrez également y trouver des produits dématérialisés comme des codes, des e-books…


MarketPlace Installation et execution:
	
	PYTHON : 3.6
	DJANGO : 1.11
	
	MODULE : mathfilters	=>	pip install django-mathfilters

	CMD	=>	cd Projet Marketplace
			python manage.py makemigrations
			python manage.py migrate
			manage.py loaddata data.json
			manage.py runserver
