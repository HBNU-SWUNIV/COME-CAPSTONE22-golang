const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('warehousing_schedule', {
    Schedule_id: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    Member_id: {
      type: DataTypes.INTEGER,
      allowNull: true,
      comment: "어떤멤버가",
      references: {
        model: 'coopMember',
        key: 'Member_id'
      }
    },
    Product_id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      comment: "어떤제품을",
      references: {
        model: 'product',
        key: 'Product_id'
      }
    },
    Shipment_amount: {
      type: DataTypes.INTEGER,
      allowNull: false,
      comment: "출하량"
    },
    Shipment_date: {
      type: DataTypes.DATEONLY,
      allowNull: false,
      comment: "예정일"
    },
    Req_price: {
      type: DataTypes.INTEGER,
      allowNull: false,
      comment: "원하는가격"
    },
    Product_quailty: {
      type: DataTypes.STRING(100),
      allowNull: true,
      comment: "상품의 품질"
    },
    Coop_id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'coop',
        key: 'Coop_id'
      }
    },
    Member_update_date: {
      type: DataTypes.DATEONLY,
      allowNull: true,
      defaultValue: Sequelize.Sequelize.fn('curdate')
    }
  }, {
    sequelize,
    tableName: 'warehousing_schedule',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "Schedule_id" },
        ]
      },
      {
        name: "Member_req_FK",
        using: "BTREE",
        fields: [
          { name: "Product_id" },
        ]
      },
      {
        name: "Member_req_FK1",
        using: "BTREE",
        fields: [
          { name: "Member_id" },
        ]
      },
      {
        name: "warehousing_schedule_FK",
        using: "BTREE",
        fields: [
          { name: "Coop_id" },
        ]
      },
    ]
  });
};
