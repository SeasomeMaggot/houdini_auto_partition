selected = hou.selectedNodes()
tupleLen = len(selected)

if tupleLen is 0:

    raise hou.Error("Select a node before operation!!!")
    
else:
  
    conNode = selected[0].node("..").createNode("connectivity", "auto_connectivity")
    hou.node(conNode.path()).setInput(0, hou.node(selected[0].path()))
    conNode.moveToGoodPosition()
    
    partNode = selected[0].node("..").createNode("partition", "auto_partition")
    hou.node(partNode.path()).setInput(0, hou.node(conNode.path()))
    partNode.moveToGoodPosition()
    partNode.setParms({"rule":"group_`@class`"})
