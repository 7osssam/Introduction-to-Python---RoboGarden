
radius = input( "Enter the radius of the circle: " ) 
if( radius.isnumeric() == False ):
	print( "Please enter a valid number" )
	exit()

Circumference = 2 * 3.14159 * float(radius)

Area = 3.14159 * float(radius) ** 2

print( "The Circumference of the circle is: ", format( Circumference, ".2f" ) )

print( "The Area of the circle is: ", format( Area, ".2f" ) )

