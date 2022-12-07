const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Simulate_Sales', {
    Sales_date: {
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    Sales_amount: {
      type: DataTypes.INTEGER,
      allowNull: false
    }
  }, {
    sequelize,
    tableName: 'Simulate_Sales',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "Sales_date" },
        ]
      },
    ]
  });
};
