from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# opening the connection, grabbing the page
uClient = uReq(my_url) # get the page urlopen(url)
page_html = uClient.read() # read the page
uClient.close() #close the connection

# html parsing with the function soup (BeautifulSoup)
# you have to tell the function how to parse the text - html.parser
page_soup = soup(page_html, "html.parser") 

# grabs each importand div in the html text, so it grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

# opening a new csv file
filename = "products.csv"

# gives a permission to write in it
file = open(filename, "w")

# setting the column names, we can do it directly in the .write() function of the file
headers = "brand, product_name, shipping\n"

# writing the column names in the file
file.write(headers)

# loop through every container and print out the extracted information
for container in containers:
	# getting the title of the product
	brand = container.div.div.a.img["title"]

	# getting the full product name
	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	# getting the shipping price
	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	# printing the results in the console
	print("brand:" + brand)
	print("product_name: " + product_name)
	print("shipping: " + shipping)
	print("")

	# writing to the file
	file.write(brand + "," + product_name.replace(",","|") + "," + shipping + "\n")

# closing the file after the writing in it is complete
file.close()