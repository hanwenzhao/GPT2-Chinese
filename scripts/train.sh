python train.py \
  #--model_config config/model_config.json \
  #--tokenized_data_path data/tokenized/ \
  #--tokenizer_path vocab/vocab.txt \
  #--data_path data/weibo_all.json \
  --epochs 30 \
  --log_step 200 \
  --stride 512 \
  --output_dir model/ \
  --device 0 \
  --num_pieces 100 \
  --raw
