## Fraud detection at self-checkouts in retail

The number of self-checkout stations is on the rise. This includes stationary self-checkouts, where customers
take their shopping cart to a scan station and pay for their products. Secondly, there are semi-stationary self-checkouts,
where customers scan their products directly and only pay at a counter. The customers either use their own smartphone
for scanning or the store provides mobile scanners. You will probably have encountered this already.

This automated process helps avoid long lines and speeds up the paying process for individual customers.
But how can retailers prevent the trust they have placed in customers from being abused? How can they decide which
purchases to check in an effort to expose fraudsters without annoying innocent customers?

## Scenario

An established food retailer has introduced a self-scanning system that allows customers to scan their items
using a handheld mobile scanner while shopping. This type of payment leaves retailers open to the risk that a certain
number of customers will take advantage of this freedom to commit fraud by not scanning all of the items in their cart.
Empirical research conducted by suppliers has shown that discrepancies are found in approximately 5 % of all self-
scan transactions. The research does not differentiate between actual fraudulent intent of the customer, inadvertent
errors or technical problems with scanners.

To minimize losses, the food retailer hopes to identify cases of fraud using targeted follow-up checks. The
challenge here is to keep the number of checks as low as possible to avoid unnecessary added expense as well as to
avoid putting off innocent customers due to false accusations. At the same time, however, the goal is to identify as
many false scans as possible.

The objective of the teams is to create a model to classify the scans as fraudulent or non-fraudulent. The
classification does not take into account whether the fraud was committed intentionally or inadvertently. To create

## this model, the teams receive information about the scans and their classification in a learning set.

## Data

Real anonymized data in the form of structured text files (csv) are provided for the task.
These files contain individual data sets.

Below are some points to note about the files:

1. Each data set is on a single line ending with "CR" ("carriage return", 0xD), “LF” (“line feed”, 0xA) or "CR" and
"LF" ("carriage return" and "line feed", 0xD and 0xA).
2. The first line (top line) has the same structure as the data sets, but contains the names of the respective columns
(data fields).
3. The top line and each data set contain several fields separated from each other by the “|” symbol.
4. Floating point numbers are not rounded. The “.” is used as the decimal separator.
5. There is no escape character, quotes are not used.
6. ASCII is the character set used.

The data sets based on which the models are to be created are listed in the “train _.csv” file_.
The data sets in the “test.csv” file should be used for the prediction.
A single data set in the files “ _train.csv”_ or “ _test.csv“_ contains information about one scanning process for one
customer, including the number of scanned items per second and the total time spent in the store.
For learning purposes, the “ _train.csv“_ file also contains a column with the classification into fraud and not fraud.


## Entries

Participants may submit their results up to and including January 15 , 20 22 , 23 :00. The task description below
explains how to submit entries

## Task

- Use historical data to create a mathematical model to reliably classify scans as fraudulent or not fraudulent.
- Complete data from the testing period will be provided.
- Data will also be provided for the subsequent testing period.
- The files “ _train.csv”_ and “t _est.csv”_ are identical in structure but differ in that the classification column is
    missing from the latter.
- Both files comply with the properties listed in the Data section.

One file containing the following information should be used to send the solution data:

There is no key attribute. The number and order of the predicted classifications must correspond to those in the
associated data sets or scans in the “ _test.csv”_ file.
The possible values for the “fraud” column are the integer values 0 or 1.
A possible excerpt from the solution file could look like this:

fraud
1
0
0
_..._

The solution file must comply with the specifications described in the Data section, as far as they are applicable.
The solution file must be uploaded as a structured text file (csv) to TEAMS.



