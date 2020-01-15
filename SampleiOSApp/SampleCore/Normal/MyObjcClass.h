//
//  MyObjcClass.h
//  SampleCore
//
//  Created by Deffrasnes Ghislain on 18/04/2019.
//  Copyright © 2019 E-Voyageurs Technologies. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>

NS_ASSUME_NONNULL_BEGIN

#define myDefinedStringConstant @"myDefinedConstant"
#define myDefinedFloatConstant 2.0f
#define myDefinedParameterConstant (@"myDefinedParameterConstant")

extern NSString *const myObjcExternConstant;
static NSString * const myStaticConstant = @"myStaticConstant";

@protocol MyObjcProtocolReference;

@protocol MyObjcProtocol <NSObject>
@end


typedef enum {
    DIRECT_ENUM_1,
    DIRECT_ENUM_2,
    DIRECT_ENUM_3
} MyDirectObjcEnum;

typedef NS_ENUM(NSUInteger, ValidationState)
{
    ValidationStateUnknown = 0,
    ValidationStateSuccess,
    ValidationStateError
};

@interface MyObjcClass : NSObject

@end

@interface ObjcViewController : UIViewController

@end

@implementation ObjcViewController

@end

NS_ASSUME_NONNULL_END
