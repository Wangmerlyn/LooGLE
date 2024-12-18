import argparse
import json
import os




def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_name", type=str, default=None, help="model name for evaluation"
    )
    parser.add_argument(
        "--task",
        type=str,
        default="longdep_qa_reorder",
        help="long context understanding tasks in LooGLE",
        choices=[
            "longdep_qa_reorder"
        ]
    )
    parser.add_argument("--output_path", type=str, default="./Output/")
    
    return parser.parse_args(args)

if __name__ == "__main__":
	args = parse_args()
	src_file = os.path.join(args.output_path + "longdep_qa" + "_" + args.model_name + ".jsonl")
	dest_file = os.path.join(args.output_path + args.task + "_" + args.model_name + ".jsonl")
	with open(src_file, "r") as f:
		data = [json.loads(line) for line in f.readlines()]
	new_jsonl = []
	for qa_pairs in data:
		for qa in qa_pairs['qa_pairs']:
			if qa['type'] == "timeline_reorder":
				new_jsonl.append(qa)