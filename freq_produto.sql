WITH tb_freq_abs AS (
SELECT descProduto,
        COUNT(idTransacao) AS FreqAbs
FROM points

GROUP BY descProduto
),


tb_freq_abs_cum AS (
SELECT *,
        SUM(FreqAbs) OVER (PARTITION BY 1 ORDER BY descProduto) AS FreqAbsAcum,
        1.0*FreqAbs / (SELECT SUM(FreqAbs) FROM tb_freq_abs) AS FreqRelativa
FROM tb_freq_abs
),

tb_freq_rel_cum AS (
SELECT *,
        SUM(FreqRelativa) OVER (ORDER BY descProduto) AS FreqRelativaCum
FROM tb_freq_abs_cum
)

SELECT *
FROM tb_freq_rel_cum
