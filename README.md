# pdfs2largeimage <!-- omit in toc -->

## 目次 <!-- omit in toc -->
- [概要](#概要)
- [環境構築](#環境構築)
- [使い方](#使い方)

## 概要
複数のPDFファイル (1ページ目のみ) を任意の行数・列数で1つの大きなPDFファイルにまとめるPythonライブラリ

## 環境構築
```bash
pip install --upgrade pip
pip install git+https://github.com/fumito100111/pdfs2largeimage.git
```

> [!TIP]
> 動作しない場合は, [pdf2imageのGitHubリポジトリ](https://github.com/Belval/pdf2image)を参考にして, popplerをインストールしてください.

## 使い方
```python
from PIL import Image # アノテーション (型ヒント)用 (任意)
from pdfs2largeimage import pdfs_to_large_image

pdf_paths: list[str] = [ # 合成するPDFファイルのパスリスト
    './**/sample1.pdf',
    './**/sample2.pdf',
    './**/sample3.pdf',
    './**/sample4.pdf',
    './**/sample5.pdf',
    './**/sample6.pdf'
]

row: int = 2    # 行数
column: int = 3 # 列数
dpi: int = 200  # 画像の解像度
save_pdf_path: str = './output/large_image.pdf' # 保存先のPDFファイルパス

large_image: Image.Image = pdfs_to_large_image(
    row=row,                    # 行数
    column=column,              # 列数
    *pdf_paths,                 # 合成するPDFファイルのパスリスト (要素数: 行数 x 列数)
    dpi=dpi,                    # 画像の解像度 (デフォルト: 200)
    save_pdf_path=save_pdf_path # 生成した画像の保存先PDFファイルパス  (保存しない場合は None (デフォルト: None))
)

# 生成した画像は以下のような順番で並びます
# +-------------------------------+-------------------------------+-------------------------------+
# |          sample1.pdf          |          sample2.pdf          |          sample3.pdf          |
# +-------------------------------+-------------------------------+-------------------------------+
# |          sample4.pdf          |          sample5.pdf          |          sample6.pdf          |
# +-------------------------------+-------------------------------+-------------------------------+
```
> [!IMPORTANT]
> 画像の1マスあたりのサイズは, 合成するPDFファイルの中で最も大きいものに合わせられます.