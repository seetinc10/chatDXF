import ezdxf

def get_shape_dimensions(shape):
    dimensions = {}
    if shape == 'circle':
        radius = float(input("Enter the radius of the circle: "))
        dimensions['radius'] = radius
    elif shape == 'square':
        side = float(input("Enter the side length of the square: "))
        dimensions['side'] = side
    elif shape == 'rectangle':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        dimensions['length'] = length
        dimensions['width'] = width
    elif shape == 'triangle':
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        dimensions['base'] = base
        dimensions['height'] = height
    else:
        print("Unknown shape.")
    return dimensions

def create_dxf(shape, dimensions):
    doc = ezdxf.new(dxfversion='R2010')
    msp = doc.modelspace()

    if shape == 'circle':
        msp.add_circle(center=(0, 0), radius=dimensions['radius'])
    elif shape == 'square':
        side = dimensions['side']
        msp.add_lwpolyline([(0, 0), (side, 0), (side, side), (0, side), (0, 0)], is_closed=True)
    elif shape == 'rectangle':
        length = dimensions['length']
        width = dimensions['width']
        msp.add_lwpolyline([(0, 0), (length, 0), (length, width), (0, width), (0, 0)], is_closed=True)
    elif shape == 'triangle':
        base = dimensions['base']
        height = dimensions['height']
        msp.add_lwpolyline([(0, 0), (base, 0), (base / 2, height), (0, 0)], is_closed=True)

    doc.saveas("shape.dxf")
    print("DXF file 'shape.dxf' created successfully.")

def main():
    print("Welcome to the geometric shape dimension collector!")
    
    shape = input("Please enter the type of shape (circle, square, rectangle, triangle): ").strip().lower()
    while shape not in ['circle', 'square', 'rectangle', 'triangle']:
        print("Invalid shape. Please enter one of the following shapes: circle, square, rectangle, triangle.")
        shape = input("Please enter the type of shape (circle, square, rectangle, triangle): ").strip().lower()
    
    dimensions = get_shape_dimensions(shape)
    
    if dimensions:
        print(f"You have entered the shape: {shape.capitalize()}")
        for dim, value in dimensions.items():
            print(f"{dim.capitalize()}: {value}")
        
        create_dxf(shape, dimensions)

if __name__ == "__main__":
    main()
