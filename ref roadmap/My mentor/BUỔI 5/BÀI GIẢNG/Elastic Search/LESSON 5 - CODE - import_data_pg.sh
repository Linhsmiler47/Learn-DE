for i in {1..20}; do
  file="products_${i}_pg.csv"
  echo "📥 Importing $file..."
  sudo -u postgres psql -d shop -c "\COPY products FROM '/opt/data_pg/$file' WITH (FORMAT csv, HEADER true)"
done
