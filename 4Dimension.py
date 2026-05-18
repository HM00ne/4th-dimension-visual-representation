from vpython import vector, rate, color, canvas, curve, label

scene = canvas(
    title="4D Cube pointed with numbers",
    width=800,
    height=600,
    background=color.black
)

points = [
    vector(-1, -1, -1),  # 0
    vector( 1, -1, -1),  # 1
    vector( 1,  1, -1),  # 2
    vector(-1,  1, -1),  # 3

    vector(-1, -1,  1),  # 4
    vector( 1, -1,  1),  # 5
    vector( 1,  1,  1),  # 6
    vector(-1,  1,  1),  # 7

    vector(-2, -2, -2),  # 8
    vector( 2, -2, -2),  # 9
    vector( 2,  2, -2),  # 10
    vector(-2,  2, -2),  # 11

    vector(-2, -2,  2),  # 12
    vector( 2, -2,  2),  # 13
    vector( 2,  2,  2),  # 14
    vector(-2,  2,  2),  # 15
]

edge_pairs = [
    (0, 1), (1, 5), (5, 4), (4, 0),
    (4, 7), (0, 3), (1, 2), (5, 6),
    (3, 7), (7, 6), (6, 2), (2, 3),

    (11, 3), (10, 2),
    (14 , 6), (15, 7),
    (12, 4), (13, 5),
    (9, 1), (8, 0),

    (8, 9), (9, 13), (13, 12), (12, 8),
    (8, 11), (9, 10), (13, 14), (12, 15),
    (14, 15), (15, 11),(11, 10), (10, 14),
]

edges = []
point_labels = []

for start, end in edge_pairs:
    edges.append(
        curve(
            pos=[points[start], points[end]],
            color=color.white,
            radius=0.03
        )
    )

for number, point in enumerate(points):
    point_labels.append(
        label(
            pos=point,
            text=str(number),
            height=18,
            color=color.green,
            box=False,
            opacity=0,
            xoffset=10,
            yoffset=10
        )
    )

while True:
        rate(60) #This is for frame rate, you can adjust it as needed

        angle = 0.001
        axis = vector(1, 1, 0)
        origin = vector(0, 0, 0)
        for edge in edges:
            edge.rotate(angle=angle, axis=axis, origin=origin)

        for point_label in point_labels:
            point_label.rotate(angle=angle, axis=axis, origin=origin)
