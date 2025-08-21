import unittest
import Program8_Solution as PS
import random

# Added just to make unit test run in order given

class TestCustomer(unittest.TestCase):

    def test01_NewCustomerSetupCorrectly(self):
        """ New Customer should have cust_number, arrived, items, items_paid,
            line_arrival, line_exit, cashier_arrival, and cashier_exit set. """

        customer = PS.Customer(1, 10, 4)
        self.assertEqual(customer.cust_number, 1, "The customer number should be set to one when passed that value ")
        self.assertEqual(customer.arrived, 10, "The customer arrived attribute should be set to value passed to it")
        self.assertEqual(customer.items, 4, "The customer items attribute should be set to value passed to it")
        self.assertEqual(customer.items_paid, 0, "The customer items_paid should be initialized to zero.")
        self.assertIs(customer.line_arrival, None, "The customer line_arrival should be initialized to None.")
        self.assertIs(customer.line_exit, None, "The customer line_exit should be initialized to None.")
        self.assertIs(customer.cashier_arrival, None, "The customer cashier_arrival should be initialized to None.")
        self.assertIs(customer.cashier_exit, None, "The customer cashier_exit should be initialized to None.")

        # Test with random customer, arrival and number of items
        cust_num = random.randint(1, 50)
        arrival = random.randint(1, 50)
        items = random.randint(1, 50)

        customer = PS.Customer(cust_num, arrival, items)
        self.assertEqual(customer.cust_number, cust_num, "The customer number should be set to one when passed that value ")
        self.assertEqual(customer.arrived, arrival, "The customer arrived attribute should be set to value passed to it")
        self.assertEqual(customer.items, items, "The customer items attribute should be set to value passed to it")
        self.assertEqual(customer.items_paid, 0, "The customer items_paid should be initialized to zero.")

    def test02_NewCustomerOutput(self):
        """ The Tests to make sure the __str__ method of Customer outputs in the proper format """
        customer = PS.Customer(2, 10, 4)
        result = str(customer)

        self.assertEqual(result, "C(2)", "The string output of the customer was not correct ")

    def test03_NewCustomerRepr(self):
        """ Tests to make sure the __repr__ method of Customer outputs in the proper format """
        customer = PS.Customer(3, 10, 4)
        result = repr(customer)

        self.assertEqual(result, "C(3)", "The string output of the customer was not correct ")

    def test04_Get_in_line(self):
        """ The method get_in_line will set the line_arrival attribute to the proper clock value """
        customer = PS.Customer(1, 10, 4)

        customer.get_in_line(20)
        self.assertEqual(customer.line_arrival, 20, "The get in line method should set the customers line_arrival")

    def test05_At_cashier(self):
        """ The method at_cashier should set the line_exit to the clock and set the arrival to the clock """
        customer = PS.Customer(1, 10, 4)

        customer.get_in_line(21)
        customer.at_cashier(22)
        self.assertEqual(customer.line_exit, 22, "The at_cashier method should set the customers line_exit")
        self.assertEqual(customer.cashier_arrival, 22, "The at_cashier method should set the customers cashier_arrival")

    def test06_Customer_update1(self):
        """ When a customer is updated if they have not arrived at cashier then items will not get decremented """
        customer = PS.Customer(1, 10, 5)

        self.assertEqual(customer.items, 5, "The number of items is initially set correctly")
        self.assertEqual(customer.items_paid, 0, "The number of paid items should not change if they are not at cashier")
        customer.update(24)
        self.assertEqual(customer.items, 5, "The number of items should not change if they are not at cashier")
        self.assertEqual(customer.items_paid, 0, "The number of paid items should not change if they are not at cashier")

    def test07_Customer_update2(self):
        """ When a customer is updated if they do not have items then items will not get decremented, even if they are at cashier """
        customer = PS.Customer(1, 10, 0)
        customer.at_cashier(25)

        self.assertEqual(customer.items, 0, "The number of items is initially set correctly")
        self.assertEqual(customer.items_paid, 0, "The number of paid items should not change if they do not have items")
        customer.update(26)
        self.assertEqual(customer.items, 0, "The number of items should not change if they are not at cashier")
        self.assertEqual(customer.items_paid, 0, "The number of paid items should not change if do not have items")

    def test08_Customer_update3(self):
        """ When a customer is updated if they have items then items  and are at the cashier, the  items are decremented and items_paid is incremented """
        customer = PS.Customer(1, 10, 3)
        customer.at_cashier(27)

        self.assertEqual(customer.items, 3, "The number of items is initially set correctly")
        self.assertEqual(customer.items_paid, 0, "The number of paid items should not change if they do not have items")
        customer.update(28)
        self.assertEqual(customer.items, 2, "The number of items should be decremented if they have items and they are at the cashier")
        self.assertEqual(customer.items_paid, 1, "The number of paid items should be incremented if they have items and are at the cashier")
        customer.update(29)
        self.assertEqual(customer.items, 1, "The number of items should be decremented if they have items and they are at the cashier")
        self.assertEqual(customer.items_paid, 2, "The number of paid items should be incremented if they have items and are at the cashier")
        customer.update(30)
        self.assertEqual(customer.items, 0, "The number of items should be decremented if they have items and they are at the cashier")
        self.assertEqual(customer.items_paid, 3, "The number of paid items should be incremented if they have items and are at the cashier")

    def test09_Customer_wait_time_returns_time_in_line(self):
        """ When a customer is updated if they have items then items  and are at the cashier, the  items are decremented and items_paid is incremented """
        customer = PS.Customer(1, 10, 3)
        customer.get_in_line(30)
        customer.at_cashier(36)

        self.assertEqual(customer.wait_time(), 6, "The person was in line for 6 units of time.")


class Test_Cashier(unittest.TestCase):

    def test10_NewCashierSetupCorrectly(self):
        """ New Customer should have lane, line, exit_pool, customer are set correctly. """
        line = []
        exit_pool = []
        cashier = PS.Cashier(1, line, exit_pool)

        self.assertEqual(cashier.lane, 1, "Lane should be set to the value passed in")
        self.assertIs(cashier.line, line, "Line should be set to the line list that is passed in.")
        self.assertIs(cashier.exit_pool, exit_pool, "exit_pool should be set to the exit pool that is passed in.")
        self.assertIs(cashier.customer, None, "Current Customer should be set to None when initialized.  There is no customer at the register")        

    def test11_Cashier_string_with_no_customer(self):
        cashier = PS.Cashier(2, [], [])
        result = str(cashier)
        self.assertEqual(result, "$(2)", "String representation should be $() with the lane number in the parens")

    def test12_Cashier_string_with_customer(self):
        cashier = PS.Cashier(3, [], [])
        cust = PS.Customer(10, 12, 4)
        cashier.customer = cust
        result = str(cashier)
        self.assertEqual(result, "$(3) - C(10)", "String representation should be $() with the lane number in the parens")

    def test13_update_Cashier_customer_is_none_then_it_takes_first_customer_from_line(self):
        cust = PS.Customer(10, 1, 4)
        line = [cust]
        exit_pool = []

        cashier = PS.Cashier(4, line, exit_pool)
        clock = 2
        cashier.update(clock)

        # After the udpate the cashier should have a customer from the line.  The line should be empty now in this case.
        self.assertIs(cashier.customer, cust, "Customer from the list should now be the customer cashier.")
        self.assertEqual(len(cashier.line), 0, "When the last customer is taken out of line the line is empty")

    def test14_update_Cashier_customer_is_none_then_it_takes_first_customer_from_line_line_has_oneleft(self):
        cust = PS.Customer(10, 1, 4)
        cust2 = PS.Customer(11, 1, 4)
        line = [cust, cust2]
        exit_pool = []

        cashier = PS.Cashier(4, line, exit_pool)
        clock = 3
        cashier.update(clock)

        # After the udpate the cashier should have a customer from the line.  The line should be empty now in this case.
        self.assertIs(cashier.customer, cust, "Customer from the list should now be the customer cashier.")
        self.assertEqual(len(cashier.line), 1, "If the list had 2 customers and one gets moved to the cashier, then the line has one less")
        self.assertIs(cashier.line[0], cust2, "Only item in listis the Customer 2. ")

    def test15_update_Cashier_customer_is_none_and_line_is_empty_no_error_is_thrown(self):
        line = []
        exit_pool = []

        cashier = PS.Cashier(4, line, exit_pool)
        clock = 4

        try:
            cashier.update(clock)   
            # After the udpate the cashier should have a customer from the line.  The line should be empty now in this case.
            self.assertIs(cashier.customer, None, "Customer from the list should now be None.")
            self.assertEqual(len(cashier.line), 0, "The line shouldn't change")
        except Exception as ex:
            self.fail("There was an error of type {} thrown when the cashier has no customer and the line is empty".format(type(ex)))

    def test16_update_Cashier_customer_is_none_then_it_takes_first_customer_from_line_and_calls_at_cashier(self):
        cust = PS.Customer(12, 1, 4)
        line = [cust]
        exit_pool = []

        cashier = PS.Cashier(6, line, exit_pool)
        clock = 5

        self.assertIs(cust.cashier_arrival, None, "The customer has not arrived at the cashier")
        self.assertIs(cust.line_exit, None, "The customer has not left the line")
        cashier.update(clock)

        # After the udpate the cashier should have a customer from the line.  The line should be empty now in this case.
        self.assertIs(cashier.customer, cust, "Customer from the list should now be the customer cashier.")
        self.assertIs(cust.cashier_arrival, clock, "The customer has not arrived at the cashier")
        self.assertIs(cust.line_exit, clock, "The customer has not left the line")

    def test17_update_Cashier_customer_has_items_reduced(self):
        cust = PS.Customer(12, 1, 4)
        line = [cust]
        exit_pool = []

        cashier = PS.Cashier(6, line, exit_pool)
        clock = 6

        cashier.update(clock)
        self.assertEqual(cust.items, 4, "The customer should have the initial amount of items")
        clock = clock + 1
        cashier.update(clock)
        self.assertEqual(cust.items, 3, "The current customer should have items reduced")

    def test18_update_Cashier_customer_when_customer_items_is_zero_then_they_leave_register_and_enter_exit_pool(self):
        cust = PS.Customer(12, 2, 1)
        line = [cust]
        exit_pool = []

        cashier = PS.Cashier(6, line, exit_pool)
        clock = 7

        cashier.update(clock)
        self.assertEqual(cust.items, 1, "The customer should have the initial amount of items")
        clock = clock + 1
        cashier.update(clock)
        self.assertEqual(cust.items, 0, "The current customer should have items reduced")
        self.assertIs(cashier.customer, None, "The customer has been removed from the register")
        self.assertEqual(len(cashier.exit_pool), 1, "The exit pool should have the customer")
        self.assertIs(cashier.exit_pool[0], cust, "The customer should be in the exit pool")


if __name__ == "__main__":
    import functools
    unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: x < y
    unittest.main()
