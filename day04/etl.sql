SELECT 
    t1.seller_id,
    SUM(t1.price) AS totalRevenue,
    COUNT(DISTINCT t1.order_id) AS qtSales
FROM tb_order_items t1
GROUP BY seller_id
