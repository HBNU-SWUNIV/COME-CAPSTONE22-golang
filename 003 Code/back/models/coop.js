const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('coop', {
    Coop_id: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    Coop_name: {
      type: DataTypes.STRING(100),
      allowNull: false,
      comment: "협동조합이름"
    },
    Coop_address: {
      type: DataTypes.STRING(100),
      allowNull: false,
      comment: "주소"
    },
    Coop_pw: {
      type: DataTypes.STRING(50),
      allowNull: false,
      comment: "비밀번호"
    },
    Coop_login_id: {
      type: DataTypes.STRING(100),
      allowNull: false,
      comment: "아이디"
    }
  }, {
    sequelize,
    tableName: 'coop',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "Coop_id" },
        ]
      },
    ]
  });
};
