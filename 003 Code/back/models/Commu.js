const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Commu', {
    post_id: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    post_category: {
      type: DataTypes.STRING(100),
      allowNull: false
    },
    author: {
      type: DataTypes.STRING(100),
      allowNull: false
    },
    text: {
      type: DataTypes.STRING(100),
      allowNull: false
    },
    post_date: {
      type: DataTypes.DATEONLY,
      allowNull: true
    },
    Coop_id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'coop',
        key: 'Coop_id'
      }
    }
  }, {
    sequelize,
    tableName: 'Commu',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "post_id" },
        ]
      },
      {
        name: "Commu_FK",
        using: "BTREE",
        fields: [
          { name: "Coop_id" },
        ]
      },
    ]
  });
};
