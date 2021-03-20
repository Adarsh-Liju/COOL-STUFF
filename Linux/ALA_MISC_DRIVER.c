#include <linux/module.h>
#include <linux/miscdevice.h>
#include <linux/fs.h>
#include <linux/poll.h>
#include <linux/errno.h>
#include <linux/init.h>

MODULE_LICENSE("GPL"); //License I used 
MODULE_AUTHOR("Adarsh Liju"); //My Name 
MODULE_DESCRIPTION("Misc Char Driver"); //What this driver is 

#define ID "PESUG20CS017" //My SRN NUMBER
#define ID_LENGTH 13    //Lenght including zero character

static ssize_t myread(struct file *file, char __user *buff, size_t count, loff_t *ppos) //for reading data
{
    char *print_string = ID;
    int len_str = ID_LENGTH;
    
    return simple_read_from_buffer(buff , count, ppos, print_string, len_str);
}

static ssize_t mywrite(struct file *file, char const __user *buff, size_t count, loff_t *ppos) //for writing data
{
    char *print_string = ID; //assigning pointers 
    char my_input[ID_LENGTH];
    int len_str = ID_LENGTH; 
    ssize_t ret_val = -EINVAL; //defined in errno.h 
    
    if (count != len_str)
        return ret_val;
    
    ret_val = simple_write_to_buffer(my_input ,count ,ppos ,buff ,count);
    
    if (ret_val < 0)
        return ret_val;
    
    return strncmp(print_string, my_input, count) ? count : -EINVAL; 
    
    return ret_val;
    
}

static const struct file_operations my_file_ops = {
    .owner = THIS_MODULE, 
    .read = myread, 
    .write = mywrite
};

static struct miscdevice my_device = {
    MISC_DYNAMIC_MINOR,
    "PESUIO", //Name 
    &my_file_ops
};

static int __init my_init(void) //Inputing
{
    int ret_two;

	ret_two = misc_register(&my_device);
	pr_debug("Hello World!"); 
	return ret_two;
}

static void __exit my_exit(void) //Exiting 
{
    misc_deregister(&my_device);
    pr_debug("Exiting");
}
// Loading and Unloading
module_init(my_init);
module_exit(my_exit);








