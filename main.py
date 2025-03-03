from polygons import PolygonType, get_polygon_coords
from plotter import plot_polygon_and_dots
from simulator import RepulsionBasedDistribution

def main():
    # ======================
    # CONFIGURATION
    # ======================
    selected_shape = PolygonType.DIAMOND 
    polygon = get_polygon_coords(selected_shape)

    density = 1
    max_iterations = 1_000
    sampler = RepulsionBasedDistribution(polygon, density, max_iterations)
    
    # ======================
    # GENERATE POINTS
    # ======================
    red_dots = sampler.generate_points()

    print(f"Generated {len(red_dots)} points with equilibrium")

    # ======================
    # VISUALIZE RESULTS
    # ======================
    plot_polygon_and_dots(
        polygon_coords=polygon,
        dots=red_dots,
        title=f"{selected_shape.name.replace('_', ' ').title()} with Mineirinho's Sampling"
    )

if __name__ == "__main__":
    main()