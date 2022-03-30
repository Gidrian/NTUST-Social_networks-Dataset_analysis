import snap


G1 = snap.TNGraph.New()
G1.AddNode(1)
G1.AddNode(5)
G1.AddNode(12)
G1.AddEdge(1,5)
G1.AddEdge(5,1)
G1.AddEdge(5,12)
NIdName = snap.TIntStrH()
NIdName[1] = "1"
NIdName[5] = "5"
NIdName[12] = "12"
snap.DrawGViz(G1, snap.gvlDot, "G1.png", "G1", NIdName)