const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('inventory', {
    Member_id: {
      type: DataTypes.INTEGER,
      allowNull: true,
      references: {
        model: 'coopMember',
        key: 'Member_id'
      }
    },
    Warehousing_amount: {
      type: DataTypes.INTEGER,
      allowNull: false
    },
    Warehousing_date: {
      type: DataTypes.DATEONLY,
      allowNull: false
    },
    Coop_id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'coop',
        key: 'Coop_id'
      }
    },
    Product_id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'product',
        key: 'Product_id'
      }
    },
    Product_quailty: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    Warehousing_id: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    Price: {
      type: DataTypes.INTEGER,
      allowNull: false
    }
  }, {
    sequelize,
    tableName: 'inventory',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "Warehousing_id" },
        ]
      },
      {
        name: "inventory_FK",
        using: "BTREE",
        fields: [
          { name: "Coop_id" },
        ]
      },
      {
        name: "inventory_FK_1",
        using: "BTREE",
        fields: [
          { name: "Member_id" },
        ]
      },
      {
        name: "inventory_FK_2",
        using: "BTREE",
        fields: [
          { name: "Product_id" },
        ]
      },
    ]
  });
};
