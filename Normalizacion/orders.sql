CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Address VARCHAR(350)
);

CREATE TABLE Phone_Types (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TypeName VARCHAR(100) NOT NULL
);

CREATE TABLE Customer_Phones (
    CustomerID INTEGER,
    PhoneNumber VARCHAR(12),
    PhoneType INTEGER,

    PRIMARY KEY (CustomerID, PhoneNumber),

    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (PhoneType) REFERENCES Phone_Types(ID)
);

CREATE TABLE Items (
    ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    ItemName VARCHAR(100) NOT NULL,
    Price DECIMAL(6,2) NOT NULL
);

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    TotalAmount DECIMAL(10,2) NOT NULL,
    OrderDate DATETIME NOT NULL,
    CustomerID INTEGER,
    DeliveryDate DATETIME,

    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE Orders_Details (
    OrderID INTEGER,
    ItemID INTEGER,
    Quantity INTEGER NOT NULL,
    Amount DECIMAL(6,2) NOT NULL,
    SpecialRequest VARCHAR(100),

    PRIMARY KEY (OrderID, ItemID),

    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
);

