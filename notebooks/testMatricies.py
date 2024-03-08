import numpy as np

def getTestMatrices():

    testMatrices = {
        "ref": np.array([
            [
                [8, 1, 7],
                [0, 5, -3],
                [0, 0, 0]
            ]
        ]), 
        
        "nonRef": np.array(
            [
               [5, 0, 1],
               [3, 2, -1]
            ] 
        ),
        
        "refGapCol": np.array(
            [
                [5, 2, -2], 
                [0, 0, 3],
                [0, 0, 0]
            ]
        ),

        "refGapCol2": np.array(
            [
                [3, -2, 6, 0, 1],
                [0, 0, 2, 7, 5],
                [0, 0, 0, -3, 5],
                [0, 0, 0, 0, 0]
            ]
        ),
        "breakPivotCol": np.array(
            [
                [3, -2, 6, 0, 1],
                [0, 0, 0, -3, 5],
                [0, 0, 2, 7, 5],
                [0, 0, 0, 0, 0]
            ]
        )

    }

    return testMatrices