const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('coopMember', {
    Member_id: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true,
      comment: "멤버아이디"
    },
    Member_name: {
      type: DataTypes.STRING(50),
      allowNull: false,
      comment: "멤버이름"
    },
    Member_pw: {
      type: DataTypes.STRING(50),
      allowNull: false,
      comment: "비밀번호"
    },
    Coop_id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      comment: "협동조합",
      references: {
        model: 'coop',
        key: 'Coop_id'
      }
    },
    Member_address: {
      type: DataTypes.STRING(100),
      allowNull: false,
      comment: "주소"
    },
    Member_phone: {
      type: DataTypes.STRING(100),
      allowNull: false,
      comment: "휴대전화"
    },
    Member_area: {
      type: DataTypes.INTEGER,
      allowNull: true
    }
  }, {
    sequelize,
    tableName: 'coopMember',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "Member_id" },
        ]
      },
      {
        name: "coopMember_FK",
        using: "BTREE",
        fields: [
          { name: "Coop_id" },
        ]
      },
    ]
  });
};
