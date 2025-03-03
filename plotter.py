import matplotlib.pyplot as plt

def plot_polygon_and_dots(polygon_coords, dots, title="Polygon with Dots"):
    """
    Plots a polygon and scatter points with consistent styling
    Args:
        polygon_coords: List of (x, y) tuples for the polygon
        dots: List of (x, y) tuples for the red points
        title: Title for the plot
    """
    # Prepare polygon coordinates (close the shape)
    x_poly = [p[0] for p in polygon_coords] + [polygon_coords[0][0]]
    y_poly = [p[1] for p in polygon_coords] + [polygon_coords[0][1]]
    
    # Prepare dots
    x_dots = [d[0] for d in dots]
    y_dots = [d[1] for d in dots]

    # Create plot
    plt.figure(figsize=(8, 6))
    plt.fill(x_poly, y_poly, 'skyblue', edgecolor='blue', linewidth=2)
    plt.scatter(x_dots, y_dots, color='red', s=50)
    
    # Formatting
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axis('equal')
    plt.show()