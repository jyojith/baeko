require 'csv'
require 'faker'

# Initialize Faker for generating random data
Faker::UniqueGenerator.clear

# Define bakery items with SKUs, names, and prices
bakery_items = [
  { sku: "SKU101", name: "Croissant", price: 2.5 },
  { sku: "SKU102", name: "Chocolate Cake", price: 15.0 },
  { sku: "SKU103", name: "Blueberry Muffin", price: 2.0 },
  { sku: "SKU104", name: "Roggenmischbrot", price: 3.0 },
  { sku: "SKU105", name: "Weißbrot", price: 2.0 },
  { sku: "SKU106", name: "Dinkelbrötchen", price: 1.5 },
  { sku: "SKU107", name: "Baguette", price: 3.5 },
  { sku: "SKU108", name: "Brezel", price: 1.0 },
  { sku: "SKU109", name: "Apple Strudel", price: 4.5 },
  { sku: "SKU110", name: "Cinnamon Roll", price: 2.2 },
  { sku: "SKU111", name: "Sourdough Bread", price: 3.8 },
  { sku: "SKU112", name: "Cherry Danish", price: 3.0 },
  { sku: "SKU113", name: "Eclair", price: 2.8 },
  { sku: "SKU114", name: "Pretzel", price: 1.2 },
  { sku: "SKU115", name: "Bagel", price: 1.8 },
  { sku: "SKU116", name: "Fruit Tart", price: 4.2 },
  { sku: "SKU117", name: "Almond Croissant", price: 3.3 },
  { sku: "SKU118", name: "Pumpernickel Bread", price: 2.7 },
  { sku: "SKU119", name: "Strawberry Shortcake", price: 5.5 },
  { sku: "SKU120", name: "Pain au Chocolat", price: 2.7 },
  # Add more items with SKUs, names, and prices...
]

# Define main cities with associated bakeries and users
main_cities = [
  {
    name: "Berlin",
    bakeries: [
      "Bäckerei Müller", "Bäckerei Schmidt", "Bäckerei Wagner"
    ],
    users: (1..30).map { |i| { name: "User#{i}", city: "Berlin" } }
  },
  {
    name: "Munich",
    bakeries: [
      "Bäckerhaus Braun", "Konditorei Meyer", "Backstube Fischer"
    ],
    users: (31..60).map { |i| { name: "User#{i}", city: "Munich" } }
  },
  {
    name: "Hamburg",
    bakeries: [
      "Brot & Butter", "Kuchenparadies", "Feine Backkunst", "LaugenHimmel"
    ],
    users: (61..90).map { |i| { name: "User#{i}", city: "Hamburg" } }
  }
]

# Generate synthetic data
num_days = 365
transactions_per_day = (10..30)  # Vary transactions per day

CSV.open("bakery_pos_data.csv", "w", write_headers: true, headers: [
  "TransactionID", "UserID", "SKU", "ProductName",
  "Quantity", "TransactionDate", "Price", "Discount",
  "PaymentMethod", "Location", "City"
]) do |csv|

  transaction_id = 10000

  num_days.times do |day|
    current_date = DateTime.new(2022, 1, 1) + day
    daily_transactions = rand(transactions_per_day)

    daily_transactions.times do
      transaction_date = current_date + rand(24 * 60) * 60  # Random time within the day
      city = main_cities.sample
      user = city[:users].sample
      num_items = rand(1..5)  # Generate random number of items in a transaction
      items = bakery_items.sample(num_items)
      total_amount = items.sum { |item| item[:price] }
      discount = rand(0.0..0.2).round(3)  # Round discount to 3 decimal places
      payment_method = ["Cash", "Card", "App"].sample
      bakery_name = city[:bakeries].sample
      location = "#{bakery_name}, #{city[:name]}"

      items.each do |item|
        csv << [
          transaction_id.to_s, user[:name], item[:sku], item[:name],
          num_items, transaction_date.strftime('%Y-%m-%d %H:%M:%S'),
          item[:price], discount, payment_method, location, city[:name]
        ]
      end

      transaction_id += 1
    end
  end
end

# Generate combined CSV file for bakery and city info
CSV.open("bakery_city_info.csv", "w", write_headers: true, headers: ["City", "Bakery"]) do |csv|
  main_cities.each do |city|
    city[:bakeries].each do |bakery|
      csv << [city[:name], bakery]
    end
  end
end

# Generate separate CSV file for user info
CSV.open("user_info.csv", "w", write_headers: true, headers: ["User", "City"]) do |csv|
  main_cities.each do |city|
    city[:users].each do |user|
      csv << [user[:name], city[:name]]
    end
  end
end
