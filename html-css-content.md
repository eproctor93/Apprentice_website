
# INTRODUCTION TO HTML & CSS

All websites use HTML and CSS  
**HTML stands for Hyper Text Markup Language  
CSS stand for Cascading style sheet**

### HTML

+ HTML stands for Hyper Text Markup Language. 
+ HTML is the standard markup language for creating Web pages.
+ HTML stands for Hyper Text Markup Language
+ HTML describes the structure of Web pages using markup
+ HTML elements are the building blocks of HTML pages
+ HTML elements are represented by tags
+ HTML tags label pieces of content such as "heading", "paragraph", "table", and so on
+ Browsers do not display the HTML tags, but use them to render the content of the page
 
a. Always put <!DOCTYPE html> on the first line. This tells the browser what language it's reading (in this case, HTML).
Things inside <>s are called tags.
Tags nearly always come in pairs: an opening tag and a closing tag eg: ```<tag> </tag>```  
b. Always put <html> on the next line. This starts the HTML document.  
c. Always put </html> on the last line. This ends the HTML document.  
Example of how tags are laid out are like this: <first tag><second tag>Some text!</second tag></first tag>
There are always two parts to an HTML file: the head and the body. Let's start with the head.

--------------------------------------------

## Head 
The head contains information about your HTML file, like its title. The title is what we see in the browser's title bar or page tab.

```
<!DOCTYPE html>
<html>
<head>
<title> My webpage! </title>	
</head>	
</html>
```
--------------------------------------------

## Paragraphs
Body is where you put your content, for example text, images & links. The body goes inside the HTML tags and after the closing <head> tag. You can write paragraphs by using the <p> tag. Don’t forget to close it. For example: 

```
<!DOCTYPE html>
<html>
<head>
<title>My Webpage</title>
</head>
<body>
<p>Hello world! </p>
<p>Welcome to this webpage</p>
</body>
```

-------------------------------------------- 

## Headings

```
HTML actually lets us have more than one heading size. There are six heading sizes, where <h1> is the biggest font size and <h6> is the smallest. 
<h1> - The CEO
<h2> - VP
<h3> - Director
<h4> - Middle management
<h5> - Lowly assistant
<h6> - Gets coffee for everyone.
For example:
```
<!DOCTYPE html>
<html>
<head>
<title>Headings & Paragraphs</title>
</head>
<body>
	<h1> Heading 1 </h1>
	  <p> This is the paragraph! </p>
	<h3> Next section </h3>
	  <p> This is another paragraph </p>
	<h5>Final section</h5>
	  <p>final paragraph</p>
</body>
</html>


## Links
There are two different types of links
```
Hyperlinks:
If you wanted to link the user to another part of your website, or another website altogether? You use hyperlinks.

To structure it, you do it like the following:
<a href="https//www.codeacademy.com">Coding tools </a>

Opening <a> tag and that tag has an attribute called href.  The href value tells your link where you want it to go for example: http://www.google.co.uk

Then you have a description of your link between your opening and your closing  tags. This is what you will be able to click on.
```

Then you have your closing tag.


Images:
To add images, we use an image tag, like so <img>. Instead of putting the content between the tags, you tell the tag where to get the picture using src. That’s the image source.


There is no ending tag and it has / in the tag to close it. <img src="url" />.

the web address (or URL) after src=? It's "https://s3.amazonaws.com/codecademy-blog/assets/f3a16fb6.jpg". That tells the <img> tag where to get the picture from!


Example:
<img src="http://www.hip-consultant.co.uk/blog/wp-content/uploads/2010/Land-Registry.jpg" />


## Ordered and Unordered lists

Ordered lists:
An ordered list is simply a list that is numbered, like the one below.

1. We begin the ordered list with the opening tag <ol>

2. On lines 9-11, we wrap(i.e. surround) each individual item with <li> </li> tags.

3. Because each listed item is only on one line, we put the entire element on one line.

4. On line 13, we finish the ordered list with the closing tag </ol>


That is all in our HTML body
```
Example:
<h1>List of my favorite things</h1>
		<ol>
			<li>Raindrops on roses</li>
			<li>Whiskers on kittens</li>
			<li>Bright copper kettles</li>
			<li>Warm woolen mittens</li>
		</ol>
<h2> Another list of my favourite things </h2>
	<ol>
	    <li> Item number one </li>
	    <li> Item number two </li>
	    <li> Item number three </li>
	    <li> Item number four </li>
	</ol>
```


## Unordered Lists

Unordered lists is when the Order doesn’t matter. But how do we do those unordered lists. 

First, we open our list with an unordered list <ul> tag For each item we wish to add to the list, we use a list item tag <li> with text in between We then tell the browser we are done with our list by calling our closing </ul> tag

```
Example:
	<h1> Some random thoughts </h1>
	<p> I have some random thoughts in my head and here is a few. </p>
	<ul>
	     <li> learning html </li>
	     <li> Happy that I have finished learning python! </li>
	     <li> Proud of my job </li>
	     <li>Other things </li> </body>
	</ul>
```  

## Nested List
Sometimes we might have an ordered list, but each item in the ordered list, but also has an unordered list. Nested simply means ‘inside’ the list.


<body>
		<ol>
			<li>Dad's interests
				<ul>
					<li>football</li>
					<li>knitting</li>
				</ul>
			</li>
			<li>Mom's interests
				<ul>
					<li>hating football</li>
					<li>skydiving</li>
				</ul>
			</li>
		</ol>
	<ul>
	    <li> Favourite Boy's Names </li>
	    <ol>
	         <li>Matthew</li>
	         <li>James</li>
	         <li>Jordan</li>
	   </ol>
	   
	    <li> Favourite Girl's Names
	    <ol>
	        <li>Jessica</li>
	        <li>Amy</li>
	        <li>Rebecca</li>
	  </ol></ul>      
	</body>


Divs 

--------------------------------------------

CSS Glossary - https://www.codecademy.com/articles/glossary-css


### CSS

CSS is a language used to style websites. Colors, font, and pages layout for a site can all be managed using CSS. The more comfortable you are with CSS, the better equipped you will be to create stylish and contemporary-looking websites.


Link to a Stylesheet?
The HTML link element links a CSS file to an HTML file so that CSS styling can be applied. Here’s an example of the link element in HTML
<link rel="stylesheet" type="text/css" href="main.css"/>
The link element uses three attributes:
rel: specifies the relationships between the current file and the file being linked to: in this case, the rel attribute is “stylesheet.”
–type: Specifies the type of linked to.
–href: Provides the URL of the file being linked to.
Like the HTML image element, link is self-closing. It does not need a closing tag.
In the example above, main.css is an external style sheet. Using external stylesheets is one of the most popular ways to write CSS. Inline CSS is another method.


# Definition 

Properties are defined within selectors by defining a property and a value. They are separated with a colon and delineated with a semi-colon.
```
Syntax
selector {
	property: value;
}
Example
h1 {
	color: blue;
	font-size: 12px;
}
```
## CSS Syntax

The element Selector
Type Selectors
The type selector targets all elements with a specific HTML tag. If we wanted to address all h1 elements, as an example, this would look like the following:
```
Example in CSS 
h1 {
	color: blue;
	font-family: verdana;
	font-size: 300%;
}


Example What it will look like in HTML
<h1>...</h1> 
```

# The id Selector  
The id selector uses the id attribute of an HTML element to select a specific element.
The id of an element should be unique within a page, so the id selector is used to select one unique element!
To select an element with a specific id, write a hash (#) character, followed by the id of the element.
The style rule below will be applied to the HTML element with id="para1
```
Example 
#para1 {
	text-align: center;
	color: red;
}
(An id selector cannot start with a numer!)
```

# The class Selector
The class selector selects elements with a specific class attribute.
To select elements with a specific class, write a period (.) character, followed by the name of the class.
In the example below, all HTML elements with class="center" will be red and center-aligned:
```
Example 
.center {
	text-align: center;
	color: red;
}
````

Grouping Selectors
Example
h1 {
	text-align: center;
	color: red;
}

p {
text-align: center;
	color: red;
}




!This section can be expanded on if needed!

## CSS Fonts
The CSS color property defines the text color to be used.
The CSS font-family property defines the font to be used.
The CSS font-size property defines the text size to be used.



