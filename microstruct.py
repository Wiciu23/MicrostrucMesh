import matplotlib.pyplot as plt
import microstructpy as msp


phase = {'shape': 'circle', 'size': 0.15}
domain = msp.geometry.Square()

# Unpositioned list of seeds
seeds = msp.seeding.SeedList.from_info(phase, domain.area)

# Position seeds in domain
seeds.position(domain)

# Create polygonal mesh
polygon_mesh = msp.meshing.PolyMesh.from_seeds(seeds, domain)

# Create triangular mesh
triangle_mesh = msp.meshing.TriMesh.from_polymesh(polygon_mesh)

# Plot outputs
for output in [seeds, polygon_mesh, triangle_mesh]:
    plt.figure()
    output.plot(edgecolor='k')
    plt.axis('image')
    plt.axis([-0.5, 0.5, -0.5, 0.5])
    plt.show()