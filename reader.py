"""
This module includes helper functions to read csv files
"""
import requests
import networkx as nx
from logging_utils import get_logger_handle, log_txt

logger = get_logger_handle(__name__)


def read_data_from_url(url:str) -> str:
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.text
    
def convert_data_into_graph(data:str) -> nx.Graph:
    record_list = data.split("\n")
    g = nx.Graph()
    for i, line in enumerate(record_list[:-1]):
        if i == 0:
            num_nodes, num_edges, _ = line.split(" ")
            logger.info(f"Expect number of nodes {num_nodes} and edges {num_edges}")
            continue
        u, v, w = line.split(" ")
        g.add_edge(int(u)-1, int(v)-1)
        logger.debug(f"Added an edge from u: {u} to  v: {v} with weight {w}")
    logger.info(f"Total number of nodes: {g.number_of_nodes()}")
    logger.info(f"Total number of edges: {g.number_of_edges()}")
    return g
        



if __name__ == "__main__":
    URL = "https://web.stanford.edu/~yyye/yyye/Gset/G15"
    data = read_data_from_url(URL)
    g = convert_data_into_graph(data)
