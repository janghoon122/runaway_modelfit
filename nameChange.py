import argparse
import os
import pandas as pd
import shutil

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, required=True, help="Data directory path")
    parser.add_argument("--label_path", type=str, required=True, help="Label information directory path")

    args = parser.parse_args()

    return args

def main(args):

    df = pd.read_csv(args.label_path)
    filename_renewed = df['file_name'].str.split('.png', expand=True)[0] + f"sep" + df['PM25'].astype('str') + f".png"

    renewed_df = pd.DataFrame()
    renewed_df['file_name'] = filename_renewed
    renewed_df['PM25'] = df['PM25']

    renewed_df.to_csv(f"{(args.label_path).split('.')[0]}_renewed.csv", index=False)

    dataRenewed_path = f"{os.path.dirname(args.data_path)}/{os.path.basename(args.data_path)}_renewed"
    os.makedirs(dataRenewed_path, exist_ok=True)

    for ii in range(len(renewed_df)):
        shutil.copy(f"{args.data_path}/{df.loc[ii]['file_name']}", f"{dataRenewed_path}/{renewed_df.loc[ii]['file_name']}")

    # shutil.copy(f"{args.data_path}21_11_18_11_22_42_875569.png", f"D:\deepvisions\data\800_1000_11_3_cropped_v2_renewed/21_11_18_11_22_42_875569sep.png")

if __name__ == "__main__":

    args = arguments()
    main(args)




