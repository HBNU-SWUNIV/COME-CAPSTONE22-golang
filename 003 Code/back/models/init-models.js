var DataTypes = require("sequelize").DataTypes;
var _Comment = require("./Comment");
var _Commu = require("./Commu");
var _Sales = require("./Sales");
var _Shipment = require("./Shipment");
var _Simulate_Sales = require("./Simulate_Sales");
var _coop = require("./coop");
var _coopMember = require("./coopMember");
var _inventory = require("./inventory");
var _product = require("./product");
var _user = require("./user");
var _warehousing_schedule = require("./warehousing_schedule");

function initModels(sequelize) {
  var Comment = _Comment(sequelize, DataTypes);
  var Commu = _Commu(sequelize, DataTypes);
  var Sales = _Sales(sequelize, DataTypes);
  var Shipment = _Shipment(sequelize, DataTypes);
  var Simulate_Sales = _Simulate_Sales(sequelize, DataTypes);
  var coop = _coop(sequelize, DataTypes);
  var coopMember = _coopMember(sequelize, DataTypes);
  var inventory = _inventory(sequelize, DataTypes);
  var product = _product(sequelize, DataTypes);
  var user = _user(sequelize, DataTypes);
  var warehousing_schedule = _warehousing_schedule(sequelize, DataTypes);

  Comment.belongsTo(Commu, { as: "post", foreignKey: "post_id"});
  Commu.hasMany(Comment, { as: "Comments", foreignKey: "post_id"});
  Commu.belongsTo(coop, { as: "Coop", foreignKey: "Coop_id"});
  coop.hasMany(Commu, { as: "Commus", foreignKey: "Coop_id"});
  coopMember.belongsTo(coop, { as: "Coop", foreignKey: "Coop_id"});
  coop.hasMany(coopMember, { as: "coopMembers", foreignKey: "Coop_id"});
  inventory.belongsTo(coop, { as: "Coop", foreignKey: "Coop_id"});
  coop.hasMany(inventory, { as: "inventories", foreignKey: "Coop_id"});
  product.belongsTo(coop, { as: "Coop", foreignKey: "Coop_id"});
  coop.hasMany(product, { as: "products", foreignKey: "Coop_id"});
  warehousing_schedule.belongsTo(coop, { as: "Coop", foreignKey: "Coop_id"});
  coop.hasMany(warehousing_schedule, { as: "warehousing_schedules", foreignKey: "Coop_id"});
  inventory.belongsTo(coopMember, { as: "Member", foreignKey: "Member_id"});
  coopMember.hasMany(inventory, { as: "inventories", foreignKey: "Member_id"});
  warehousing_schedule.belongsTo(coopMember, { as: "Member", foreignKey: "Member_id"});
  coopMember.hasMany(warehousing_schedule, { as: "warehousing_schedules", foreignKey: "Member_id"});
  Sales.belongsTo(product, { as: "Product", foreignKey: "Product_id"});
  product.hasMany(Sales, { as: "Sales", foreignKey: "Product_id"});
  Shipment.belongsTo(product, { as: "Product", foreignKey: "Product_id"});
  product.hasMany(Shipment, { as: "Shipments", foreignKey: "Product_id"});
  inventory.belongsTo(product, { as: "Product", foreignKey: "Product_id"});
  product.hasMany(inventory, { as: "inventories", foreignKey: "Product_id"});
  warehousing_schedule.belongsTo(product, { as: "Product", foreignKey: "Product_id"});
  product.hasMany(warehousing_schedule, { as: "warehousing_schedules", foreignKey: "Product_id"});

  return {
    Comment,
    Commu,
    Sales,
    Shipment,
    Simulate_Sales,
    coop,
    coopMember,
    inventory,
    product,
    user,
    warehousing_schedule,
  };
}
module.exports = initModels;
module.exports.initModels = initModels;
module.exports.default = initModels;
