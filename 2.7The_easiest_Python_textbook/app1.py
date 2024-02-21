# 再度計算を実行します
# まず、4秒間のサンプリング回数を計算します。
sampling_rate = 10000  # 10kHz
sampling_duration = 4  # 4秒
number_of_samples = sampling_rate * sampling_duration

# 各サンプリングデータを16ビット＝2バイトで量子化するためのデータ量を計算します。
bits_per_sample = 16
bytes_per_sample = bits_per_sample / 8  # 1バイトは8ビット
quantized_data_size = number_of_samples * bytes_per_sample

# ADPCMで1/4に圧縮されたデータ量を計算します。
compression_ratio = 1/4
compressed_data_size = quantized_data_size * compression_ratio

# 圧縮後のデータ量をkバイト単位で計算します。
compressed_data_size_kb = compressed_data_size / 1000  # 1kバイトは1000バイト

# 結果を表示します。
print(f"サンプリングデータ量: {quantized_data_size}バイト")

