import sys
import pandas as pd

arg_names = [
        'path_localstore', 
        'path_centralstore',
        'path_data',
        'graph_id',
        'partition_id',
    ]

args = dict(zip(arg_names, sys.argv[1:]))

path_nodes_localstore = args['path_localstore'] + args['graph_id'] + '_attributes_' + args['partition_id']
nodes_localstore = pd.read_csv(path_nodes_localstore , sep='\s+', lineterminator='\n',header=None)
nodes_localstore.set_index(0,inplace=True)

path_edges_localstore = args['path_localstore'] + args['graph_id'] + '_' + args['partition_id']
edges_localstore = pd.read_csv(path_edges_localstore, sep='\s+', lineterminator='\n', header=None)
edges_localstore.columns = ["source","target"] 

path_nodes_centralstore = args['path_centralstore'] + args['graph_id'] + '_centralstore_attributes_' + args['partition_id']
nodes_centralstore = pd.read_csv(path_nodes_localstore , sep='\s+', lineterminator='\n',header=None)
nodes_centralstore.set_index(0,inplace=True)

path_edges_centralstore = args['path_centralstore'] + args['graph_id'] + '_' + args['partition_id']
edges_centralstore = pd.read_csv(path_edges_localstore, sep='\s+', lineterminator='\n', header=None)
edges_centralstore.columns = ["source","target"]

nodes = pd.concat([nodes_localstore,nodes_centralstore]).reset_index().drop_duplicates(subset=[0]).set_index(0)
edges = pd.concat([edges_localstore,edges_centralstore],ignore_index=True)

path_nodes = args['path_data'] + args['graph_id'] + '_nodes_' + args['partition_id'] + ".csv"
path_edges = args['path_data'] + args['graph_id'] + '_edges_' + args['partition_id'] + ".csv"

nodes.to_csv(path_nodes)
edges.to_csv(path_edges,index=0)

