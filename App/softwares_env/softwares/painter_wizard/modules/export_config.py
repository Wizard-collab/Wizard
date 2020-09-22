json_config = {
        "exportShaderParams": False,
        "exportPath": "",
        "defaultExportPreset" : "wizard_PBR",
        "exportPresets": [
            {
                "name": "wizard_PBR",
                "maps": [
                    {
                        "fileName": "",
                        "channels": [
                            {
                                "destChannel": "R",
                                "srcChannel": "R",
                                "srcMapType": "documentMap",
                                "srcMapName": "baseColor"
                            },
                            {
                                "destChannel": "G",
                                "srcChannel": "G",
                                "srcMapType": "documentMap",
                                "srcMapName": "baseColor"
                            },
                            {
                                "destChannel": "B",
                                "srcChannel": "B",
                                "srcMapType": "documentMap",
                                "srcMapName": "baseColor"
                            },
                        ]
                    },
                    {
                        "fileName": "",
                        "channels": [
                            {
                                "destChannel": "L",
                                "srcChannel": "L",
                                "srcMapType": "documentMap",
                                "srcMapName": "roughness"
                            },
                        ]
                    },
                    {
                        "fileName": "",
                        "channels": [
                            {
                                "destChannel": "L",
                                "srcChannel": "L",
                                "srcMapType": "documentMap",
                                "srcMapName": "metallic"
                            },
                        ]
                    },
                    {
                        "fileName": "",
                        "channels": [
                            {
                                "destChannel": "R",
                                "srcChannel": "R",
                                "srcMapType": "documentMap",
                                "srcMapName": "normal"
                            },
                            {
                                "destChannel": "G",
                                "srcChannel": "G",
                                "srcMapType": "documentMap",
                                "srcMapName": "normal"
                            },
                            {
                                "destChannel": "B",
                                "srcChannel": "B",
                                "srcMapType": "documentMap",
                                "srcMapName": "normal"
                            },
                            {
                                "destChannel": "A",
                                "srcChannel": "A",
                                "srcMapType": "documentMap",
                                "srcMapName": "normal"
                            },
                        ]
                    },
                    {
                        "fileName": "",
                        "channels": [
                            {
                                "destChannel": "L",
                                "srcChannel": "L",
                                "srcMapType": "documentMap",
                                "srcMapName": "height"
                            },
                        ]
                    },
                    {
                        "fileName": "",
                        "channels": [
                            {
                                "destChannel": "L",
                                "srcChannel": "L",
                                "srcMapType": "documentMap",
                                "srcMapName": "user0"
                            },
                        ]
                    }]
            }],
        "exportList": [],
        "exportParameters": [
            {
                "parameters": {
                    "fileFormat" : "",
                    "bitDepth" : "32f",
                    "dithering": False,
                    "paddingAlgorithm": "infinite"
                }
            }]
        }