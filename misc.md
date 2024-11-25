# Misc.

## SOLID principle

SOLID stands for the five design principles:
- **Single responsiblility**
- **Open/Closed:** software entites should be open for extension, closed for modification (ex: visitor pattern)
- **Liskov substitution:** objects of a superclass by be substituted for objects of a subclass without breaking the application.
- **Interface segregation:** a class should not be forced to implement methods that it does not need.
- **Dependency inversion:** high-level modules should not depend on abstractions and not import anything from low-level modules.

### Example of the Interface Segregation Principle

```php
interface Customers {
    public function getAddress();
    public function getVipPoints();
}

class VIPCustomer {
    public function getAddress() {
        // ...
    }
    
    public function getVipPoints() {
        // ...
    }
}


interface BasicCustomer {
    public function getAddress() {
        // ...
    }

    // should not be forced to implement this
    public function getVipPoints() {
        // ...
    }
}
```

### Example of the Dependency Inversion Principle

```php

// High-level module
class User {
    
    public string $userEmail;

    // Dependency is injected via the constructor
    public function __construct(private IEmailService emailService) {
    }

    public function notifyUser() {
        $this->emailService->sendEmail($this->userEmail);
    }
}

interface IEmailService {
    public function sendEmail();
}

class EmailServiceImpl implements IEmailService {
    public function sendEmail(string $userEmail) {
        // send email
    }
}

// Set up the DI container
$container = new Container();

$container['EmailService'] = function () {
    return new EmailServiceImpl();
};

$container['User'] = function ($c) {
    return new User($c['EmailService']);
};

// Use the container to resolve dependencies
$userService = $container['UserService'];
$userService->notifyUser("test@example.com");
```

### Example of Liskov Substitution

https://stackoverflow.com/questions/56860/what-is-an-example-of-the-liskov-substitution-principle

## Polymorphism and inheritance

Inheritance is when a class inherits methods and properties from another class. Polymorphism is the act of using this methods to perform various tasks. Polymorphism means differents forms.

```php
class GeometricObject () {
    public function draw() {}
}

class Square extends GeometricObject {
    public function draw() {}
}

class Triangle extends GeometricObject {
    public function draw() {}
}


$square = new Square();
$triange = new Triangle();

// results of both draw() methods will not be the same
$square->draw();
$triange->draw();
```

## SCRUM & Agile

TBP

## Waterfall

TBP