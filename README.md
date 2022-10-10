# bhargabchipkg
bhargabchipkg (pronounced “Bhargab chi package”) is an open-source package for applying chi square (a statistical test) which is helpful for mathematics, science, and engineering. Chi square is already written package available with scipy. But, this package(bhargabchipkg) will help you to sort out the salesman ranks (good or bad)

It is applicable for sales data having minimum three columns:
 salesman id (or name, etc having more than one level).
 saleflag i.e. 0 and 1 where 0 refers unsold and 1 refers sold.
 type of item (only two levels i.e. two types of items).

It takes four inputs:
1. a dataframe with categorical columns for input as well as output
2. Input categorical column name (more than one level)
3. Output categorical column name(should have two levels 0 and 1. Where 0 refers unsold and 1 refers sold)
4. Groupby column name(should have two levels)
the column name must be passed as string (inside double inverted commas)

You can find the example datasheet from this link: 
You can see the output from this link: 

How to install our package?

pip install bhargabchipkg


Website: https://www.businessbrio.com/

Source code:https://github.com/bhargabganguli/bhargabchipkg.git

Bug reports: https://github.com/bhargabganguli/bhargabchipkg/issues


License
Â© 2022 Bhargab Ganguli

This repository is licensed under the MIT license. 
See  https://github.com/bhargabganguli/bhargabchipkg/blob/0.0.4/LICENSE   for details.
