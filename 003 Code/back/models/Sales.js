const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Sales', {
    Sales_id: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    Sales_amount: {
      type: DataTypes.INTEGER,
      allowNull: false
    },
    Sales_price: {
      type: DataTypes.INTEGER,
      allowNull: false
    },
    Sales_date: {
      type: DataTypes.DATEONLY,
      allowNull: false
    },
    Product_id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'product',
        key: 'Product_id'
      }
    },
    Sales_buyer: {
      type: DataTypes.STRING(100),
      allowNull: false
    }
  }, {
    sequelize,
    tableName: 'Sales',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "Sales_id" },
        ]
      },
      {
        name: "Sales_FK",
        using: "BTREE",
        fields: [
          { name: "Product_id" },
        ]
      },
    ]
  });
};
