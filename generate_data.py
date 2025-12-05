import json
import os
from pathlib import Path

from tqdm import tqdm


def main(output_path: Path = Path("./data.json")):
    result = {
        "title": "LOGO x 材質 融合問卷",
        "instructionExamples": {
            "good": [
                {
                    "title": "範例一",
                    "logo": "images/samples/s1_logo.jpg",
                    "material": "images/samples/s1_material.jpg",
                    "result": "images/samples/s1_result.jpg",
                },
                {
                    "title": "範例二",
                    "logo": "images/samples/s3_logo.jpg",
                    "material": "images/samples/s3_material.jpg",
                    "result": "images/samples/s3_result.jpg",
                },
                {
                    "title": "範例三",
                    "logo": "images/samples/s4_logo.jpg",
                    "material": "images/samples/s4_material.jpg",
                    "result": "images/samples/s4_result.jpg",
                },
            ],
            "structureLoss": {
                "logo": "images/samples/unitednations.jpg",
                "material": "images/samples/yarn_04.jpg",
                "result": "images/samples/result_42_8.jpg",
            },
            "textureLoss": {
                "logo": "images/samples/unitednations.jpg",
                "material": "images/samples/yarn_04.jpg",
                "result": "images/samples/result_4_44.jpg",
            },
            "textureLoss2": {
                "logo": "images/samples/pepsi.jpg",
                "material": "images/samples/custom_12.jpg",
                "result": "images/samples/pepsi_custom_12_controlnet.png",
            },
        },
        "cases": [],
    }

    images_path = Path("./images")
    case_dirs = [file for file in os.listdir(images_path) if os.path.isdir(images_path / file) and file.startswith("q")]

    for case_name in tqdm(case_dirs):
        result["cases"].append(
            {
                "id": case_name,
                "logo": f"images/{case_name}/logo.png",
                "material": f"images/{case_name}/texture.png",
                "options": [
                    {
                        "value": "ours",
                        "image": f"images/{case_name}/ours.png",
                    },
                    {
                        "value": "self_rectification",
                        "image": f"images/{case_name}/self_rectification.png",
                    },
                    {
                        "value": "material_fusion",
                        "image": f"images/{case_name}/material_fusion.png",
                    },
                    {
                        "value": "controlnet",
                        "image": f"images/{case_name}/controlnet.png",
                    },
                ],
            }
        )

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
